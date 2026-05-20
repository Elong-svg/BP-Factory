#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一键处理脚本 - 自动完成检查 + 修复
"""

import sys
import os
import subprocess

# 切换到脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def main():
    if len(sys.argv) < 2:
        print("用法：python process.py 输入.md [--output 输出.md]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == '--output' else input_file.replace('.md', '_processed.md')
    
    print("\n" + "=" * 80)
    print("[Markdown 一键处理]")
    print("=" * 80)
    print(f"\n[输入] {input_file}")
    print(f"[输出] {output_file}")
    print("=" * 80)
    
    # Step 1: 检查标题
    print("\n[Step 1] 检查标题结构...")
    print("-" * 80)
    subprocess.run([sys.executable, "check_headings.py", input_file])
    
    # Step 2: 修复标题
    print("\n[Step 2] 修复标题...")
    print("-" * 80)
    subprocess.run([sys.executable, "fix_headings.py", input_file, output_file])
    
    # Step 3: 再次检查
    print("\n[Step 3] 验证修复结果...")
    print("-" * 80)
    subprocess.run([sys.executable, "check_headings.py", output_file])
    
    print("\n" + "=" * 80)
    print("[完成] 一键处理完成！")
    print(f"[输出] {output_file}")
    print("=" * 80)

if __name__ == '__main__':
    main()
