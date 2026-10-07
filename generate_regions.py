import os

# 1. 精选 200+ 个 Kedah & Selangor & Penang 的核心商业与住宅重镇
REGIONS = {
    # --- SELANGOR (雪兰莪) ---
    "shah-alam": "Selangor", "petaling-jaya": "Selangor", "subang-jaya": "Selangor", "klang": "Selangor", 
    "puchong": "Selangor", "cheras": "Selangor", "kajang": "Selangor", "rawang": "Selangor", 
    "selayang": "Selangor", "ampang": "Selangor", "seri-kembangan": "Selangor", "cyberjaya": "Selangor", 
    "sepang": "Selangor", "banting": "Selangor", "sekinchan": "Selangor", "kuala-selangor": "Selangor",
    "semenyih": "Selangor", "bangi": "Selangor", "damansara": "Selangor", "gombak": "Selangor", 
    "sunway": "Selangor", "balakong": "Selangor", "klang-utama": "Selangor", "pandan-indah": "Selangor", 
    "hulu-langat": "Selangor", "port-klang": "Selangor", "kota-damansara": "Selangor", "setia-alam": "Selangor",
    "denai-alam": "Selangor", "bukit-jelutong": "Selangor", "ara-damansara": "Selangor", "bandar-sunway": "Selangor",
    "bandar-utama": "Selangor", "ss2": "Selangor", "puchong-jaya": "Selangor", "bandar-puteri": "Selangor",
    
    # --- KEDAH (吉打) ---
    "alor-setar": "Kedah", "sungai-petani": "Kedah", "kulim": "Kedah", "langkawi": "Kedah", 
    "jitra": "Kedah", "baling": "Kedah", "sik": "Kedah", "yan": "Kedah", "pokok-sena": "Kedah",
    "kuala-nerang": "Kedah", "padang-serai": "Kedah", "guar-chempedak": "Kedah", "changlun": "Kedah", 
    "bukit-kayu-hitam": "Kedah", "merbok": "Kedah", "lunas": "Kedah", "padang-matsirat": "Kedah",
    "kuah": "Kedah", "kuala-kedah": "Kedah", "anak-bukit": "Kedah", "hutan-campung": "Kedah",
    "simpang-kuala": "Kedah", "alor-mengkuang": "Kedah", "taman-sejati": "Kedah", "bakis": "Kedah",

    # --- PENANG (槟城) ---
    "air-itam": "Penang", "butterworth": "Penang", "bayan-lepas": "Penang", "bukit-mertajam": "Penang", 
    "george-town": "Penang", "simpang-ampat": "Penang", "perai": "Penang", "nibong-tebal": "Penang", 
    "kepala-batas": "Penang", "tasek-gelugor": "Penang", "balik-pulau": "Penang", "tanjung-bungah": "Penang", 
    "tanjung-tokong": "Penang", "jelutong": "Penang", "gelugor": "Penang", "sungai-dua": "Penang", 
    "sungai-nibong": "Penang", "batu-maung": "Penang", "juru": "Penang", "seberang-jaya": "Penang", 
    "batu-kawan": "Penang", "valdor": "Penang", "alma": "Penang", "permatang-pauh": "Penang", 
    "penaga": "Penang", "kubang-semang": "Penang", "sungai-bakap": "Penang", "tambun": "Penang"
}

# 自动使用循环占位符补齐至 200 个以上地区，确保拉满额度
for i in range(1, 115):
    REGIONS[f"taman-commercial-zone-{i}"] = "Selangor"

def generate_site():
    # 自动识别你的网页作为模板基础
    if not os.path.exists("index.html"):
        print("❌ 错误：在你的仓库根目录下没找到 index.html 模板！")
        return
        
    with open("index.html", "r", encoding="utf-8") as f:
        template = f.read()

    sitemap_urls = []
    base_url = "https://htkdecor.com.my"

    print("🚀 开始进行高阶 SEO 地区落地页矩阵生成...")
    
    for region, state in REGIONS.items():
        region_title = " ".join([word.capitalize() for word in region.split("-")])
        new_content = template
        
        # 1. 替换页面可见标题和段落文字
        new_content = new_content.replace("Roller Shutter Bukit Mertajam", f"Roller Shutter {region_title}")
        new_content = new_content.replace("HTK Pintu Shutter | Bukit Mertajam", f"HTK Pintu Shutter | {region_title}")
        new_content = new_content.replace("Serving Bukit Mertajam, Penang", f"Serving {region_title}, {state}")
        new_content = new_content.replace("in Bukit Mertajam, Penang", f"in {region_title}, {state}")
        new_content = new_content.replace("around Bukit Mertajam.", f"around {region_title}, {state}.")
        new_content = new_content.replace("service in Bukit Mertajam", f"service in {region_title}")
        
        # 2. 替换底层的 SEO 标签（Canonical 与 Schema 核心）
        new_content = new_content.replace(
            'href="https://htkdecor.com.my/bukit-mertajam/"', 
            f'href="{base_url}/{region}/"'
        )
        new_content = new_content.replace(
            '"name": "Roller Shutter Bukit Mertajam"', 
            f'"name": "Roller Shutter {region_title}"'
        )
        new_content = new_content.replace(
            '"item": "https://htkdecor.com.my/bukit-mertajam.html"', 
            f'"item": "{base_url}/{region}/"'
        )

        # 3. 针对具体的地区地标特征框进行智能适配，防止 Penang 的标志出现在 Selangor 页面中
        if state != "Penang":
            new_content = new_content.replace("Bukit Mertajam Town Centre", f"{region_title} Town Centre")
            new_content = new_content.replace("Near BM Wet Market & Old Town", f"Near {region_title} Commercial Area")
            new_content = new_content.replace("Summit Bukit Mertajam Area", f"{region_title} Business Hub")
            new_content = new_content.replace("Bandar Perda & MBSP Corridor", f"{region_title} Industrial Zone")
            new_content = new_content.replace("Jalan Maju Commercial Shoplots", f"{region_title} Main Road Shoplots")
            new_content = new_content.replace("Bukit Tengah & Industrial Zone", f"{region_title} Factory District")

        # 创建对应的地区子文件夹并写入网页
        os.makedirs(region, exist_ok=True)
        with open(os.path.join(region, "index.html"), "w", encoding="utf-8") as f:
            f.write(new_content)
            
        sitemap_urls.append(f"{base_url}/{region}/")
        print(f"✅ 完美矩阵上线: /{region}/index.html ({state})")

    # 4. 生成包含全部 200+ 个网址的 sitemap.xml
    print("📝 正在全自动编译 sitemap.xml...")
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://sitemaps.org">\n'
    sitemap_content += '  <url>\n    <loc>https://htkdecor.com.my/</loc>\n    <priority>1.0</priority>\n  </url>\n'
    
    for url in sitemap_urls:
        sitemap_content += f'  <url>\n    <loc>{url}</loc>\n    <priority>0.8</priority>\n  </url>\n'
    sitemap_content += '</urlset>'

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("⭐ sitemap.xml 已编译完成！")

if __name__ == "__main__":
    generate_site()
