from PIL import Image
import os, glob

wallpaper_dir = r'C:\Users\ErrorX\WorkBuddy\20260403192133\xcarus-blog\static\hero-wallpapers'

jpgs = glob.glob(os.path.join(wallpaper_dir, '*.jpg')) + glob.glob(os.path.join(wallpaper_dir, '*.jpeg'))
if not jpgs:
    print("No JPG files found!")
    exit(1)

print(f"Found {len(jpgs)} wallpapers\n")

total_before = 0
total_after = 0

for jpg in jpgs:
    fname = os.path.basename(jpg)
    base = os.path.splitext(fname)[0]
    webp_path = os.path.join(wallpaper_dir, base + '.webp')

    img = Image.open(jpg)
    if img.mode in ('RGBA', 'P', 'LA'):
        img = img.convert('RGBA')
    else:
        img = img.convert('RGB')

    img.save(webp_path, 'WEBP', quality=75)

    orig = os.path.getsize(jpg)
    new = os.path.getsize(webp_path)
    total_before += orig
    total_after += new
    pct = round((1 - new/orig) * 100, 1)
    print(f"  ✅ {base}.webp  ({orig//1024}KB → {new//1024}KB, -{pct}%)")

print(f"\n{'='*50}")
print(f"Total: {total_before//1024}KB → {total_after//1024}KB (-{round((1-total_after/total_before)*100,1)}%)")
print(f"Saved: {(total_before-total_after)//1024}KB")
