#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
标题修复脚本 - 最终成功版！

功能：
1. ## 标题 → 第 X 章
2. ### 标题 → 根据编号判断层级：
   - X.Y → ### X.Y（节）
   - X.Y.Z → #### X.Y.Z（小节）

铁律：只改标题，不动内容！
"""

import sys
import os
import re

def count_dots(text):
    """计算编号中的点数"""
    # 提取编号部分（数字和点）
    match = re.match(r'^(\d+(\.\d+)*)', text.strip())
    if match:
        num_str = match.group(1)
        return num_str.count('.')
    return 0

def main():
    if len(sys.argv) < 2:
        print("用法：python fix_headings_FINAL_WORKING.py 输入.md [输出.md]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.replace('.md', '_fixed.md')
    
    print(f"\n[输入] {input_file}")
    print(f"[输出] {output_file}")
    print("=" * 80)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    
    # 计数器
    chapter = 0        # 第几章
    section = 0        # 第几节
    subsection = 0     # 第几小节
    
    # 跳过标记
    skip_until_next_chapter = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # ========== 处理 ## 标题 ==========
        if line.startswith('## ') and not line.startswith('### '):
            text = stripped[3:]  # 去掉"## "
            
            # 执行摘要 - 保留
            if "执行摘要" in text:
                new_lines.append("## 执行摘要\n")
                print(f"行{i+1:4d}: ## 执行摘要")
                chapter = 0
                continue
            
            # 参考文献 - 检查是否是真的参考文献
            if "参考文献" in text:
                # 检查后面 5 行内是否有以数字开头的行（真正的参考文献格式：1. xxx）
                is_real = False
                for j in range(i+1, min(i+6, len(lines))):
                    next_line = lines[j].strip()
                    if re.match(r'^\d+\.', next_line):
                        is_real = True
                        break
                
                if is_real:
                    # 是真的参考文献
                    new_lines.append("\n## 参考文献\n")
                    print(f"行{i+1:4d}: ## 参考文献")
                else:
                    # 假的参考文献，跳过
                    print(f"行{i+1:4d}: [跳过] 假的参考文献")
                continue
            
            # 跳过"结论"（不含"投资"）
            if "结论" in text and "投资" not in text:
                print(f"行{i+1:4d}: [跳过] {text}")
                skip_until_next_chapter = True
                continue
            
            # 新章节开始
            chapter += 1
            section = 0
            subsection = 0
            skip_until_next_chapter = False
            
            chapter_names = {
                1: "行业分析",
                2: "财务分析",
                3: "战略分析"
            }
            
            name = chapter_names.get(chapter, "")
            chapter_chinese = "一二三四五六七八九十"[chapter-1]
            
            new_lines.append(f"\n## 第{chapter_chinese}章 {name}\n")
            print(f"行{i+1:4d}: ## 第{chapter_chinese}章 {name}")
            continue
        
        # ========== 处理 ### 标题 ==========
        elif line.startswith('### '):
            if skip_until_next_chapter:
                print(f"行{i+1:4d}: [跳过] {stripped}")
                continue
            
            text = stripped[4:]  # 去掉"### "
            
            # 计算编号中的点数
            dots = count_dots(text)
            
            # 清理旧编号
            clean = re.sub(r'^\d+(\.\d+)*\s*', '', text)
            clean = re.sub(r'^[一二三四五六七八九十]+[、.]', '', clean)
            clean = re.sub(r'^第.+?章\s*', '', clean)
            
            # 根据点数判断层级
            if dots >= 2:
                # 两位数字（如 1.2.1）→ #### X.Y.Z（小节）
                subsection += 1
                if chapter == 0:
                    new_line = f"#### {section}.{subsection} {clean}\n"
                else:
                    new_line = f"#### {chapter}.{section}.{subsection} {clean}\n"
                print(f"行{i+1:4d}: #### {text:35s} → {new_line.strip()}")
            
            else:
                # 一位数字（如 1.2）→ ### X.Y（节）
                section += 1
                subsection = 0  # 重置小节计数
                if chapter == 0:
                    new_line = f"### {section} {clean}\n"
                else:
                    new_line = f"### {chapter}.{section} {clean}\n"
                print(f"行{i+1:4d}: ### {text:40s} → {new_line.strip()}")
            
            new_lines.append(new_line)
            continue
        
        # ========== 其他行 - 原样保留 ==========
        else:
            new_lines.append(line)
    
    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print("\n" + "=" * 80)
    print(f"[完成] 已保存到：{output_file}")
    print("=" * 80)
    print("\n[结构说明]")
    print("  ## → 第 X 章")
    print("  ### → X.Y（节）")
    print("  #### → X.Y.Z（小节）")
    print("=" * 80)

if __name__ == '__main__':
    main()
