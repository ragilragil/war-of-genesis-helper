#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auto-translate War of Genesis Helper from Vietnamese to Indonesian
"""

import re
import sys

# Dictionary Vietnam → Indonesia (sorted by length descending to avoid partial matches)
TRANSLATIONS = {
    # Long phrases first
    "Dữ Liệu & Chiến Lược Toàn Diện": "Data & Strategi Lengkap",
    "Thống Kê DPS Kỹ Năng (Combat Breakdown)": "Statistik DPS Skill (Combat Breakdown)",
    "Bảng Xếp Hạng Hiệu Suất Cày Vàng & EXP AFK (Money/s & EXP/s)": "Leaderboard Performa Farming Gold & EXP AFK (Money/s & EXP/s)",
    "Tổng Sát Thương Gây Ra": "Total Damage yang Diberikan",
    "Thống Kê DPS & Sát Thương Chi Tiết Từng Kỹ Năng Hero": "Statistik DPS & Damage Detail Per Skill Hero",
    "Tổng Vàng mỗi lần Clear": "Total Gold per Clear",
    "Tổng EXP mỗi lần Clear": "Total EXP per Clear",
    "Ghi lại các trận": "Catat semua battle",
    "Boss Thế Giới": "World Boss",
    "Nhấn vào một trận để xem chi tiết DPS từng chiêu": "Klik battle untuk lihat detail DPS per skill",
    "Kỹ Năng Huấn Luyện (Nâng Vàng)": "Skill Training (Upgrade Gold)",
    "Kỹ Năng Huấn Luyện": "Skill Training",
    "Cây Kỹ Năng (Tự Lưu & Điểm Cấp)": "Skill Tree (Auto Save & Poin Level)",
    "Kỹ Năng Bị Động": "Skill Pasif",
    "Mở menu: Kỹ Năng Huấn Luyện & Trang Bị Toàn Game": "Buka menu: Skill Training & Equipment Full Game",
    "Xem Cây Kỹ Năng": "Lihat Skill Tree",
    "Tổng Số Ngọc Sở Hữu": "Total Gem yang Dimiliki",
    "Bảng Xếp Hạng": "Leaderboard",
    "Ải hiện tại": "Stage sekarang",
    "Lực chiến": "Combat Power",
    "Cây Kỹ Năng": "Skill Tree",
    "Kỹ Năng": "Skill",
    "Tổng cấp": "Total level",
    "Tên Kỹ Năng": "Nama Skill",
    "Tổng Số": "Total",
    "Tổng máu quái": "Total HP monster",
    "Tổng Vàng": "Total Gold",
    "Tổng EXP": "Total EXP",
    "Đột Kích": "Raid",
    "Tổng Sát Thương": "Total Damage",
    
    # Common words
    "điểm": "poin",
    "Dễ": "Mudah",
    "Khó": "Sulit",
    "Thường": "Normal",
    "Giải": "Clear",
    "Tổng": "Total",
    "Sở Hữu": "Dimiliki",
    "Chi Tiết": "Detail",
    "Từng": "Per",
    "Hiệu Suất": "Performa",
    "Cày": "Farming",
    "Xếp Hạng": "Ranking",
}

def translate_file(input_path, output_path):
    """Read file, translate, and write back"""
    print(f"Reading: {input_path}")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_size = len(content)
    replacements = 0
    
    # Sort by length (descending) to replace longer phrases first
    sorted_translations = sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)
    
    for viet, indo in sorted_translations:
        if viet in content:
            count = content.count(viet)
            content = content.replace(viet, indo)
            replacements += count
            print(f"  ✓ '{viet}' → '{indo}' ({count}x)")
    
    # Change lang attribute
    content = content.replace('lang="vi"', 'lang="id"')
    
    print(f"\nWriting: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    new_size = len(content)
    print(f"✅ Done! {replacements} replacements | Size: {original_size:,} → {new_size:,} bytes")

if __name__ == '__main__':
    translate_file('index.html', 'index.html')
    print("\n🎉 Translation complete!")
