#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown 文件一键拼接脚本
功能：将多个 Markdown 文件直接合并成一个文件

用法：
    # 合并多个文件
    python merge.py 输出.md 输入 1.md 输入 2.md 输入 3.md
    
    # 从文件列表读取
    python merge.py 输出.md --file-list files.txt
"""

import sys
import os
import argparse

def merge_files(output_file, input_files, skip_lines_config=None):
    """
    合并多个 Markdown 文件
    
    Args:
        output_file: 输出文件路径
        input_files: 输入文件列表
        skip_lines_config: 字典，指定每个文件要跳过的行数 {file_index: skip_count}
    """
    print(f"\n[合并任务] 开始合并 {len(input_files)} 个文件")
    print(f"[输出文件] {output_file}")
    print("=" * 60)
    
    total_lines = 0
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i, input_file in enumerate(input_files):
            if not os.path.exists(input_file):
                print(f"[错误] 文件不存在：{input_file}")
                continue
            
            # 获取要跳过的行数
            skip_lines = skip_lines_config.get(i, 0) if skip_lines_config else 0
            
            print(f"[{i+1}/{len(input_files)}] {input_file}", end="")
            if skip_lines > 0:
                print(f" (跳过前{skip_lines}行)", end="")
            
            with open(input_file, 'r', encoding='utf-8') as infile:
                lines = infile.readlines()
                
                # 跳过指定行数
                if skip_lines > 0:
                    lines = lines[skip_lines:]
                
                # 写入内容
                for line in lines:
                    outfile.write(line)
                    total_lines += 1
            
            print(f" [完成]")
    
    print("=" * 60)
    print(f"[合并完成] 总共 {total_lines} 行")
    print(f"[输出文件] {output_file}")
    
    # 显示文件大小
    file_size = os.path.getsize(output_file)
    print(f"[文件大小] {file_size/1024:.1f}KB")

def main():
    parser = argparse.ArgumentParser(
        description='Markdown 文件一键拼接工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 合并多个文件
  python merge.py output.md file1.md file2.md file3.md
  
  # 第二个文件跳过前 10 行（删除重复标题）
  python merge.py output.md file1.md file2.md --skip 0 10 0
  
  # 从文件列表读取
  python merge.py output.md --file-list files.txt
        """
    )
    
    parser.add_argument('output', help='输出文件路径')
    parser.add_argument('inputs', nargs='*', help='输入文件列表')
    parser.add_argument('--file-list', '-f', help='包含文件列表的文本文件')
    parser.add_argument('--skip', '-s', nargs='*', type=int, 
                       help='每个文件要跳过的行数（空格分隔）')
    
    args = parser.parse_args()
    
    # 获取输入文件列表
    input_files = args.inputs.copy()
    
    # 从文件列表读取
    if args.file_list:
        if not os.path.exists(args.file_list):
            print(f"[错误] 文件列表不存在：{args.file_list}")
            sys.exit(1)
        
        with open(args.file_list, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    input_files.append(line)
    
    if not input_files:
        print("[错误] 请提供至少一个输入文件")
        print("\n用法:")
        print("  python merge.py 输出.md 输入 1.md 输入 2.md")
        print("  python merge.py 输出.md --file-list files.txt")
        sys.exit(1)
    
    # 解析跳过行数配置
    skip_config = {}
    if args.skip:
        for i, skip_count in enumerate(args.skip):
            if skip_count > 0:
                skip_config[i] = skip_count
    
    # 执行合并
    merge_files(args.output, input_files, skip_config)

if __name__ == '__main__':
    main()
