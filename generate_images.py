#!/usr/bin/env python3
"""Generate sidexside social media images using Gemini API."""

import json, base64, time, os, sys
import urllib.request

API_KEY = "AIzaSyDA6Ne0kx03gfP0zJQsobsyHcnH_fTMUZo"
MODEL = "gemini-2.0-flash-exp-image-generation"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
OUT_DIR = os.path.join(os.path.dirname(__file__), "images")
os.makedirs(OUT_DIR, exist_ok=True)

PROMPTS = {
    "b2b-01-campus-golden-hour": "Professional editorial photograph: Two young diverse college-age women walking together on a beautiful tree-lined university campus pathway at golden hour. Shot from behind at medium distance, showing the full campus environment. They carry backpacks and walk side by side naturally. Warm golden light filters through the trees. The campus is lush and inviting. Shot on 35mm film, slight grain. Professional university marketing style photography. The mood is warm, connected, and aspirational.",

    "b2b-02-campus-pathway": "Professional architectural photograph: Wide shot of a beautiful ivy-league style university campus pathway at dusk. Warm pathway lights glow along a tree-lined walkway. A few students visible in the distance walking in pairs. Historic campus buildings frame the scene. The lighting is warm and inviting -- blue hour with warm accent lights. Professional editorial style. The mood is prestigious, welcoming, and institutional.",

    "b2b-03-walking-together-side": "Professional editorial photograph: Two young diverse college-age women (one Black, one Asian) walking side by side on a university campus sidewalk, talking and smiling naturally. Shot from the side at waist level with shallow depth of field. Blue sky visible, campus buildings softly blurred in background. Golden hour warm light. They wear casual college clothes. The mood is natural, connected, and authentic. Professional university brochure style photography.",

    "b2b-04-campus-buildings": "Professional architectural photograph: Beautiful university campus buildings at golden hour. Red brick or stone collegiate architecture with columns and arched windows. No people. Warm sunlight casting long shadows across a manicured quad. Trees with autumn or spring foliage. Shot in clean, crisp editorial style. The image should feel prestigious, established, and aspirational. University marketing photography style.",

    "b2b-05-group-walking": "Professional editorial photograph: Three diverse college-age women walking together on a wide university campus sidewalk, laughing naturally. Shot from slightly behind and to the side, showing the campus environment ahead of them. They carry backpacks. Golden hour light. Campus buildings and trees in background. 35mm film photography style. The mood is joyful, connected, and authentic. University lifestyle photography.",

    "b2b-06-night-campus-lights": "Professional cinematic photograph: A beautiful university campus at night with warm pathway lights lining a walkway. Two young women walk together in the middle distance, silhouetted by warm light. The campus architecture is visible with warm interior lights glowing from windows. Blue-purple night sky. The mood is warm, inviting, and secure-feeling. Professional editorial style. Moody but positive atmosphere.",

    "b2b-07-library-exit": "Professional editorial photograph: Two young diverse college women exiting a grand university library building at dusk, walking together down stone steps. They carry backpacks and books. Warm dusk lighting with the library's interior glowing behind them. The architecture is impressive and collegiate. Shot from a lower angle to emphasize the building. 35mm film style. The mood is academic, connected, and aspirational.",

    "b2b-08-quad-aerial": "Professional aerial photograph: Bird's eye view of a beautiful university quadrangle with crisscrossing pathways, green lawns, mature trees, and groups of students walking in pairs and small groups along the paths. The pattern of pathways creates a natural geometric design. Warm afternoon light casts interesting shadows. The campus looks vibrant and alive. Clean, crisp professional drone photography style.",

    "b2b-09-entering-campus": "Professional editorial photograph: Two diverse college-age women entering through grand wrought-iron university gates at golden hour. The gates are flanked by brick pillars. They carry backpacks and walk confidently together. The university campus is visible through the gates - green lawns, trees, buildings. Warm golden sunlight from behind creates a slight lens flare. Shot on 35mm film. The mood is welcoming, aspirational, and empowering.",

    "b2b-10-campus-steps": "Professional editorial photograph: A diverse group of four college-age women sitting together on wide stone steps of a university building, talking and laughing. The architecture is grand and collegiate. Warm afternoon light. They have backpacks and books around them. One is looking at her phone. The mood is social, connected, and natural. Shot in editorial university lifestyle style. 35mm film grain.",

    "b2b-11-night-walking-pair": "Professional cinematic photograph: Two young diverse women walking together on a well-lit university campus sidewalk at night. Warm streetlamp glow illuminates them. They are talking and smiling. One gestures while speaking. Campus buildings with glowing windows in background. The mood is warm, connected, and comforting despite being nighttime. Editorial photography style with slight film grain.",

    "b2b-12-campus-crosswalk": "Professional editorial photograph: Two young diverse college-age women crossing a campus road together at a crosswalk, shot from a dynamic low angle. Blue sky above. University buildings visible. They walk confidently side by side. Warm golden hour light. The image feels energetic and purposeful. 35mm film photography style. University marketing aesthetic.",
}

def generate_image(name, prompt):
    out_path = os.path.join(OUT_DIR, f"{name}.png")
    if os.path.exists(out_path):
        print(f"  SKIP {name} (already exists)")
        return True

    payload = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]}
    }).encode()

    req = urllib.request.Request(URL, data=payload, headers={"Content-Type": "application/json"})
    try:
        resp = urllib.request.urlopen(req, timeout=120)
        data = json.loads(resp.read())
    except Exception as e:
        print(f"  FAIL {name}: {e}")
        return False

    for c in data.get("candidates", []):
        for p in c.get("content", {}).get("parts", []):
            if "inlineData" in p:
                img_bytes = base64.b64decode(p["inlineData"]["data"])
                with open(out_path, "wb") as f:
                    f.write(img_bytes)
                print(f"  OK   {name} ({len(img_bytes)//1024}KB)")
                return True

    print(f"  FAIL {name}: no image in response")
    if "candidates" in data:
        for c in data["candidates"]:
            fr = c.get("finishReason", "")
            if fr:
                print(f"        finishReason: {fr}")
    return False

if __name__ == "__main__":
    print(f"Generating {len(PROMPTS)} images...\n")
    success = 0
    for i, (name, prompt) in enumerate(PROMPTS.items()):
        print(f"[{i+1}/{len(PROMPTS)}] {name}")
        if generate_image(name, prompt):
            success += 1
        if i < len(PROMPTS) - 1:
            time.sleep(3)  # rate limit buffer
    print(f"\nDone: {success}/{len(PROMPTS)} images generated in {OUT_DIR}")
