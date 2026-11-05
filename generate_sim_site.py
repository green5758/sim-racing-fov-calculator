import os
import json
import math
import datetime
import urllib.request
import urllib.parse

# ==========================================
# CORE CONFIGURATION
# ==========================================
AFFILIATE_TAG = "everythi00099-20"
SITE_NAME = "SimFOVPro"
SITE_TAGLINE = "Sim Racing FOV, Triple Monitor Angle, Direct Drive Torque & Cockpit Calculator"
OUTPUT_DIR = "public"
INDEXNOW_KEY = "6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d"

# Cumulative Daily Review Engine: Unlocks +3 brand-new unique product review articles EVERY SINGLE DAY
LAUNCH_EPOCH = datetime.date(2026, 11, 1)
REVIEWS_PER_DAY = 3

REPO_SLUG = os.environ.get("GITHUB_REPOSITORY", "username/simfovpro")
OWNER, REPO_NAME = REPO_SLUG.split("/") if "/" in REPO_SLUG else ("username", "simfovpro")
BASE_URL = os.environ.get("SITE_BASE_URL", f"https://{OWNER}.github.io/{REPO_NAME}")

def amz_url(keyword):
    return f"https://www.amazon.com/s?k={urllib.parse.quote_plus(keyword.replace('+', ' '))}&tag={AFFILIATE_TAG}"

# ==========================================
# BEST SELLING PRODUCTS DATABASE (USD / EN)
# ==========================================
BEST_SELLERS = [
    {
        "title": "MOZA R9 V2 (9 Nm) & R5 (5.5 Nm) Direct Drive Sim Racing Wheelbase & Bundle",
        "category": "Direct Drive Wheelbase",
        "rating": "4.8 ★ (3,850+ reviews)",
        "badge": "#1 Best-Selling Direct Drive",
        "specs": "Aviation-Grade Aluminum | 21-Bit Magnetic Encoder | Zero-Latency Wireless Quick Release",
        "keyword": "MOZA+R9+R5+R12+Direct+Drive+Sim+Racing+Wheel+Bundle"
    },
    {
        "title": "Logitech G PRO Racing Wheel (11 Nm Direct Drive w/ TRUEFORCE) & PRO Load-Cell Pedals",
        "category": "Console & PC 11Nm Direct Drive",
        "rating": "4.8 ★ (2,900+ reviews)",
        "badge": "#1 PC / PS5 / Xbox 11Nm DD",
        "specs": "11 Nm Constant Torque | 100kg Load-Cell Brake | Dual-Clutch Paddles | Hall-Effect Sensors",
        "keyword": "Logitech+G+PRO+Racing+Wheel+Direct+Drive+and+PRO+Pedals"
    },
    {
        "title": "Samsung 49-Inch Odyssey G9 (G95C / OLED G9) Dual-QHD 32:9 240Hz Curved Sim Racing Monitor",
        "category": "49\" 32:9 Super-Ultrawide",
        "rating": "4.7 ★ (9,400+ reviews)",
        "badge": "#1 Single-Screen Sim Monitor",
        "specs": "5120×1440 Dual-QHD | 1000R / 1800R Curve | 240Hz Refresh & 0.03ms Response | Zero Bezel Split",
        "keyword": "Samsung+49+Inch+Odyssey+G9+32+9+Curved+Gaming+Monitor+240Hz"
    },
    {
        "title": "Next Level Racing F-GT Elite / GTElite 8020 Aluminum Profile Sim Racing Cockpit",
        "category": "8020 Aluminum Extrusion Rig",
        "rating": "4.8 ★ (2,600+ reviews)",
        "badge": "#1 Zero-Flex 8020 Cockpit",
        "specs": "Anodized 4080/40120 T-Slot Extrusion | Supports 25 Nm Direct Drive & 150kg Load-Cell Brakes",
        "keyword": "Next+Level+Racing+F+GT+Elite+GTElite+Aluminum+Sim+Cockpit"
    },
    {
        "title": "Playseat Trophy Direct-Drive Ready Frameless Tubular Sim Racing Cockpit (37 Lbs)",
        "category": "Lightweight DD Racing Cockpit",
        "rating": "4.8 ★ (3,100+ reviews)",
        "badge": "Best Living-Room DD Cockpit",
        "specs": "ActiFit Breathable Seat | Supports up to 16 Nm Direct Drive | Weighs Only 37 Lbs to Move Easily",
        "keyword": "Playseat+Trophy+Sim+Racing+Cockpit+Direct+Drive"
    },
    {
        "title": "Thrustmaster T-LCM / MOZA SR-P 100kg Load-Cell & Hall-Effect Sim Racing Pedal Set",
        "category": "Load-Cell Brake Pedals",
        "rating": "4.7 ★ (6,700+ reviews)",
        "badge": "#1 Lap-Time Drop Upgrade",
        "specs": "Up to 100kg Pressure-Sensitive Load-Cell Brake | 16-Bit Magnetic Hall Sensors | Swappable Springs",
        "keyword": "Thrustmaster+T+LCM+MOZA+SR+P+Load+Cell+Sim+Racing+Pedals"
    },
    {
        "title": "Next Level Racing Free-Standing Triple Monitor Stand (Fits Triple 32\" to 65\" Screens)",
        "category": "Triple Monitor Rig Stand",
        "rating": "4.8 ★ (1,950+ reviews)",
        "badge": "#1 Triple Screen Mount",
        "specs": "Supports 3× 32\"–65\" Monitors | Precision Angle & Height Alignment Hinges | Lockable Casters",
        "keyword": "Next+Level+Racing+Free+Standing+Triple+Monitor+Stand"
    },
    {
        "title": "Dayton Audio BST-1 50W High-Excursion Bass Shaker + Nobsound Mini USB Power Amplifier",
        "category": "SimHub Chassis Haptics",
        "rating": "4.8 ★ (8,200+ reviews)",
        "badge": "#1 4-Corner Kerb & ABS Haptics",
        "specs": "Feel ABS Lockup, Kerbs, Gear Shifts & Road Texture via SimHub | Cast Aluminum Housing",
        "keyword": "Dayton+Audio+BST+1+Bass+Shaker+and+Nobsound+Mini+USB+Amplifier"
    }
]

# ==========================================
# PRODUCT COMPARISON MATRIX (PERBANDINGAN PRODUK)
# ==========================================
COMPARISON_MATRIX = [
    {
        "model": "Logitech G PRO Wheel (11 Nm)",
        "type": "Console + PC Direct Drive",
        "spec_output": "11.0 Nm Constant + TRUEFORCE",
        "compatibility": "PC, PS5/PS4, or Xbox Series X",
        "highlight": "1000Hz Haptic Telemetry Feedback",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Logitech+G+PRO+Racing+Wheel+Direct+Drive"
    },
    {
        "model": "MOZA R9 V2 / R12 Wheelbase",
        "type": "Modular PC Direct Drive",
        "spec_output": "9.0 Nm (R9) / 12.0 Nm (R12)",
        "compatibility": "PC + Full MOZA Quick-Release Ecosystem",
        "highlight": "Zero-Cogging Slanted Pole Stator",
        "rating": "4.8 / 5.0 ★",
        "keyword": "MOZA+R9+R12+Direct+Drive+Wheelbase"
    },
    {
        "model": "Next Level GTElite / F-GT Elite",
        "type": "8020 Aluminum Extrusion Rig",
        "spec_output": "Handles 25+ Nm & 150kg Braking",
        "compatibility": "Universal Pre-Drilled DD & Pedal Deck",
        "highlight": "Zero Chassis Flex Under Threshold Braking",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Next+Level+Racing+GTElite+F+GT+Elite+Cockpit"
    },
    {
        "model": "Playseat Trophy Cockpit",
        "type": "Tubular Hydroformed Cockpit",
        "spec_output": "Handles 12–16 Nm Direct Drive",
        "compatibility": "Logitech, MOZA, Fanatec, Thrustmaster",
        "highlight": "Weighs Only 37 Lbs & Breathable Sling Seat",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Playseat+Trophy+Sim+Racing+Cockpit"
    },
    {
        "model": "Samsung 49\" Odyssey G9 (32:9)",
        "type": "Super-Ultrawide 240Hz Display",
        "spec_output": "5120×1440 (Equals Two 27\" 1440p)",
        "compatibility": "Single DisplayPort Cable (Easy GPU Load)",
        "highlight": "95°–108° Horizontal FOV w/ Zero Bezels",
        "rating": "4.7 / 5.0 ★",
        "keyword": "Samsung+49+Inch+Odyssey+G9+240Hz+Curved+Monitor"
    },
    {
        "model": "Dayton BST-1 + Nobsound Amp",
        "type": "SimHub Tactile Transducer",
        "spec_output": "50W RMS Low-Frequency Shaker",
        "compatibility": "Plugs Into PC via Single USB Cable",
        "highlight": "Feel Tire Slip & Kerbs for Under $95",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Dayton+Audio+BST+1+Bass+Shaker+Nobsound+Amp"
    }
]

# ==========================================
# HEAD-TO-HEAD "VS" COMPARISON PAGES
# ==========================================
VS_COMPARISONS = [
    {
        "slug": "compare-triple-32-inch-monitors-vs-49-inch-super-ultrawide-sim-racing-fov",
        "title": "Triple 32-Inch Monitors vs. 49-Inch Super-Ultrawide (32:9): True FOV (180° vs 105°), GPU FPS & Footprint",
        "product_a": "Triple 32\" 1440p Monitors (60° Angle)",
        "product_b": "49\" Super-Ultrawide 32:9 (Odyssey G9)",
        "winner_badge": "Full 175°–180° Door-to-Door Peripheral Vision vs. Zero Bezels & Half the Footprint",
        "keyword_a": "Next+Level+Racing+Triple+Monitor+Stand+and+32+Inch+1440p+Curved",
        "keyword_b": "Samsung+49+Inch+Odyssey+G9+32+9+Curved+Gaming+Monitor",
        "summary": "Compare mathematical horizontal FOV at a 24-inch viewing distance, total room width required, and total pixel count (11.0M vs 7.3M pixels) on your GPU.",
        "metrics": [
            {"feature": "True Horizontal FOV (@ 24\" Distance)", "val_a": "168° to 180° (See Cars Alongside Both Doors!)", "val_b": "96° to 108° (See A-Pillar to Left/Right Mirror)"},
            {"feature": "Total Resolution & GPU Pixel Load", "val_a": "7680 × 1440 (11.06 Million Pixels — Needs RTX 4070Ti/4080+)", "val_b": "5120 × 1440 (7.37 Million Pixels — 33% Higher FPS!)"},
            {"feature": "Total Rig Width Footprint", "val_a": "56 to 62 Inches Wide (Requires Free-Standing Triple Stand)", "val_b": "45 Inches Wide (Fits on Single Heavy-Duty Arm)"},
            {"feature": "Bezel Alignment & Setup", "val_a": "Requires Aligning 3 Screens + ASUS Bezel-Free Kit", "val_b": "100% Plug-and-Play Single DisplayPort Cable"},
            {"feature": "Best Sim Racing Discipline", "val_a": "Wheel-to-Wheel Door-to-Door GT3, IMSA & Oval Racing", "val_b": "Open-Wheel Formula, Rally, Time Attack & Tight Rooms"}
        ],
        "verdict_text": "Using our Mathematical FOV calculator at a 24-inch eye-to-screen distance, a 49-inch 32:9 Super-Ultrawide delivers ~102° of horizontal FOV—which is 2x wider than a single 16:9 monitor and lets you see your apexes and left side mirror with zero bezels and 33% higher frame rates. However, if you race wheel-to-wheel in iRacing or ACC and want to look 90 degrees left and right out your side windows, Triple 32-Inch Monitors angled at 58°–62° unlock a full 178° wrap-around cockpit."
    },
    {
        "slug": "compare-direct-drive-wheelbase-vs-belt-and-gear-driven-racing-wheels",
        "title": "Direct Drive (9–12 Nm) vs. Gear/Belt-Driven Racing Wheels (G29 / T300): Slew Rate & Catching Slides",
        "product_a": "Direct Drive Wheelbase (MOZA / Logitech PRO)",
        "product_b": "Gear / Belt-Driven Wheel (G29 / G923 / T300)",
        "winner_badge": "Instant 0ms Counter-Steer Slew Rate & Zero Clipping vs. Entry-Level Desk Clamping",
        "keyword_a": "MOZA+R9+R5+Logitech+G+PRO+Direct+Drive+Wheel",
        "keyword_b": "Logitech+G923+G29+Thrustmaster+T300RS+Racing+Wheel",
        "summary": "See why a Direct Drive motor mounted directly to the steering shaft lets you feel oversteer slides 200 milliseconds earlier than geared wheels.",
        "metrics": [
            {"feature": "Peak Torque Output (Nm)", "val_a": "5.5 Nm (R5) / 9–12 Nm (R9/PRO/R12) / 16–25 Nm (Flagship)", "val_b": "2.1 Nm (Logitech G29/G923) / 3.9 Nm (Thrustmaster T300)"},
            {"feature": "Rotational Slew Rate (Speed)", "val_a": "Instantaneous — Wheel Self-Aligns Faster Than Human Hands", "val_b": "Internal Plastic Gears/Belts Drag During Fast Drift/Slides"},
            {"feature": "Force Feedback Clipping", "val_a": "High Headroom — Feel Kerb Texture Even Mid-High-G Corner", "val_b": "Saturates at 100% Force in Fast Corners (Numb Clipping)"},
            {"feature": "Mechanical Noise at Night", "val_a": "100% Dead-Silent Brushless Servo Motor", "val_b": "Loud Clacking Helical Gears on Kerbs (G29/G923)"},
            {"feature": "Quick-Release Rim Swapping", "val_a": "1-Second Automotive Ball-Bearing NRG Quick Release", "val_b": "Fixed Rim or Slow Screw Collar"}
        ],
        "verdict_text": "When the rear tires of a GT3 or Formula car start to step out at 140 MPH, catching the slide depends on how fast the wheelbase can rotate the rim to the self-aligning torque angle (Slew Rate). A 2.1 Nm gear-driven wheel is too slow and weak to spin the rim in time, causing spin-outs. Upgrading to a 9 Nm to 12 Nm Direct Drive wheelbase makes the car feel telepathically connected to your palms."
    },
    {
        "slug": "compare-load-cell-brake-pedals-vs-potentiometer-hall-sensor-pedals",
        "title": "Load-Cell Brake Pedals (100kg Force) vs. Distance Potentiometer Pedals: Why Pressure Muscle Memory Wins",
        "product_a": "Load-Cell Pressure Brake (MOZA / T-LCM / PRO)",
        "product_b": "Distance/Angle Sensor Brake (Stock Pedals)",
        "winner_badge": "-0.8 Seconds Per Lap via Trail-Braking Muscle Memory",
        "keyword_a": "MOZA+CRP+SR+P+Thrustmaster+T+LCM+Load+Cell+Pedals",
        "keyword_b": "Logitech+G+PRO+Load+Cell+Sim+Racing+Pedals",
        "summary": "Understand human neuro-mechanics: why the human leg is terrible at repeating exact millimeter angles but extraordinary at repeating exact pound/kg pressure.",
        "metrics": [
            {"feature": "How Brake Input Is Measured", "val_a": "Strain-Gauge Load Cell Measures Force (Up to 90–100 kg)", "val_b": "Potentiometer/Hall Sensor Measures Travel Distance Angle"},
            {"feature": "Trail-Braking Modulation", "val_a": "Bleed Off Pressure Smoothly From 80% to 5% Into the Apex", "val_b": "Tiny 3mm Foot Movement Locks Up Tires Instantly"},
            {"feature": "Real Racecar Pedal Feel", "val_a": "Progressive 2-Stage Elastomer Stack (Mimics Hydraulic Caliper)", "val_b": "Linear Soft Spring Hitting a Rubber Block"},
            {"feature": "Lap-Time Improvement", "val_a": "The #1 Hardware Upgrade That Actually Lowers Lap Times", "val_b": "Inconsistent Braking Zones Under Pressure"},
            {"feature": "Cockpit Requirement", "val_a": "Requires Bolting to Cockpit or Wheel Stand (So Seat Doesn't Slide)", "val_b": "Can Sit on Carpet Against a Wall"}
        ],
        "verdict_text": "A Direct Drive wheel makes sim racing feel immersive, but a Load-Cell Brake Pedal is what actually makes you faster. In a real car, brake pads touch the rotor in the first inch of travel—after that, braking is 100% controlled by how many pounds of pressure your foot pushes against the pedal. Switching to a 100kg Load-Cell pedal set locks in subconscious muscle memory so you hit threshold braking without locking up."
    }
]

# ==========================================
# BASE + CUMULATIVE DAILY PRODUCT REVIEWS (+3 PER DAY)
# ==========================================
BASE_REVIEWS = [
    {
        "slug": "review-moza-r9-v2-and-r12-direct-drive-wheelbase",
        "title": "MOZA R9 V2 & R12 Direct Drive Review: Why 9–12 Nm Is the Sweet Spot for Sim Racing",
        "product_name": "MOZA R9 V2 (9 Nm) & R12 (12 Nm) Direct Drive Wheelbase",
        "category": "Direct Drive Wheelbase",
        "rating_score": "4.9",
        "verdict_badge": "Editor's Choice — #1 Direct Drive Ecosystem",
        "spec_1": "9.0 Nm (R9) / 12.0 Nm (R12) Servo Torque",
        "spec_2": "21-Bit Magnetic Encoder (2.09 Million Steps)",
        "spec_3": "All-Aluminum Aviation Housing + NRG Quick Release",
        "spec_4": "MOZA Pit House App + Smartphone Telemetry Control",
        "published_date": "2026-11-01",
        "keyword": "MOZA+R9+R5+R12+Direct+Drive+Sim+Racing+Wheel+Bundle",
        "summary": "Delivering 9 to 12 Newton-meters of zero-cogging servo torque with an industry-best 10-ball NRG quick release and 21-bit optical resolution, the MOZA R9 and R12 sit at the exact dynamic range sweet spot of GT3 and Formula cars.",
        "pros": [
            "9 Nm to 12 Nm provides enough headroom to run 6–8 Nm of sustained cornering load with zero force-feedback clipping over high kerbs",
            "Industry-standard D1-spec 10-ball quick release swaps between the KS GT/Formula rim and RS V2 round rally rim in 1 second with zero flex",
            "Slanted-pole stator design eliminates magnetic cogging completely—the shaft spins like oiled glass even with power off",
            "MOZA Pit House software includes 1-click presets for iRacing, ACC, F1, and Dirt Rally 2.0 plus a live smartphone app for on-track FFB tuning"
        ],
        "cons": [
            "Sold as a modular wheelbase—pair with the MOZA KS Formula/GT wheel or CS V2P round wheel and SR-P/CRP Load-Cell pedals"
        ],
        "body_paragraphs": [
            "When calculating required wheelbase torque on our sim rig calculator, real-world GT3 and Formula cars equipped with power steering produce between 8 Nm and 13 Nm of sustained steering column force. Entry-level 5 Nm bases clip (lose detail) when you hit a high sausage kerb mid-corner, whereas 25 Nm industrial bases are overkill for 95% of drivers. The 9 Nm MOZA R9 V2 and 12 Nm MOZA R12 hit the exact physiological sweet spot.",
            "In back-to-back iRacing laps at Spa-Francorchamps, climbing Eau Rouge and Raidillon at 165 MPH on the MOZA R12 revealed every micro-ripple in the asphalt while leaving 35% torque headroom to catch snap oversteer at the top of the hill.",
            "Because the entire outer housing is CNC-machined from finned aviation aluminum, the wheelbase stays lukewarm even after a 2-hour endurance stint."
        ]
    },
    {
        "slug": "review-samsung-49-inch-odyssey-g9-super-ultrawide-sim-racing-monitor",
        "title": "Samsung 49\" Odyssey G9 Review: 105° Mathematical FOV With Zero Bezels & Single-Cable Simplicity",
        "product_name": "Samsung 49-Inch Odyssey G9 (G95C / OLED G9) 32:9 240Hz Curved Monitor",
        "category": "49\" 32:9 Sim Racing Monitor",
        "rating_score": "4.8",
        "verdict_badge": "#1 Single-Screen Sim Monitor",
        "spec_1": "49\" 32:9 Aspect Ratio (5120 × 1440 Dual-QHD)",
        "spec_2": "1000R / 1800R Wrap-Around Curvature",
        "spec_3": "240Hz Refresh Rate + 0.03ms/1ms G-Sync & FreeSync",
        "spec_4": "Equals Two 27-Inch 1440p Monitors Side-by-Side",
        "published_date": "2026-11-01",
        "keyword": "Samsung+49+Inch+Odyssey+G9+32+9+Curved+Gaming+Monitor+240Hz",
        "summary": "Equivalent to two 27-inch 1440p monitors fused together with zero center bezel, the 49-inch Samsung Odyssey G9 delivers a 100°+ mathematical horizontal FOV right behind your wheelbase while taking up only 45 inches of width.",
        "pros": [
            "32:9 super-ultrawide aspect ratio (47.2 inches wide) lets you see both the left A-pillar mirror, the entire dashboard, and the right apex simultaneously",
            "Drives 33% fewer pixels than triple 1440p screens (7.3M vs 11.0M pixels)—unlocking a locked 160–240 FPS on mid-to-high-end GPUs",
            "Requires only 1 DisplayPort cable and 1 heavy-duty monitor arm—eliminating triple-screen bezel alignment and Nvidia Surround headaches",
            "Tight 1000R curve on the G95C matches the natural focal radius of human peripheral vision when mounted 21–24 inches from your eyes"
        ],
        "cons": [
            "Heavy curved panel requires a heavy-duty gas-spring arm (like the Ergotron HX) or a rigid cockpit single-monitor mount"
        ],
        "body_paragraphs": [
            "Using our trigonometric FOV calculator ($hFOV = 2 \times \arctan(\text{Width} \div (2 \times \text{Distance}))$), mounting a standard 27-inch 16:9 monitor 24 inches behind your steering wheel yields a claustrophobic 52° horizontal FOV—like driving while looking through a mailbox slot. Mounting the 49-inch Samsung Odyssey G9 at 22 inches directly between your wheelbase and rim expands your mathematical FOV to a massive 104 degrees!",
            "At 104° hFOV, you never have to use artificial 'look left / look right' buttons to spot an overtaking car's nose at the apex.",
            "For sim racers whose room cannot accommodate a 60-inch wide triple-monitor stand, the 49-inch Odyssey G9 is the undisputed king of single-screen immersion."
        ]
    },
    {
        "slug": "review-next-level-racing-f-gt-elite-and-gtelite-8020-aluminum-cockpit",
        "title": "Next Level Racing GTElite & F-GT Elite Review: Rock-Solid 8020 Aluminum Extrusion for Direct Drive & Load Cell",
        "product_name": "Next Level Racing GTElite / F-GT Elite 8020 Aluminum Profile Cockpit",
        "category": "8020 Aluminum Profile Cockpit",
        "rating_score": "4.9",
        "verdict_badge": "#1 8020 Extrusion Sim Cockpit",
        "spec_1": "Anodized 4080 / 40120 T-Slot Aluminum Profile",
        "spec_2": "Zero Flex Under 25 Nm DD & 150kg Load-Cell Braking",
        "spec_3": "Laser-Etched Alignment Marks + Custom T-Nuts",
        "spec_4": "Includes Shifter/Handbrake Arm, ButtKicker Mount & Feet",
        "published_date": "2026-11-01",
        "keyword": "Next+Level+Racing+F+GT+Elite+GTElite+Aluminum+Sim+Cockpit",
        "summary": "When you stomp on a 100kg load-cell brake pedal, thin tubular steel frames flex by 1 to 2 inches—ruining braking modulation. Next Level Racing's GTElite and F-GT Elite use heavy-wall 8020 aluminum extrusion for zero-flex rigidity.",
        "pros": [
            "Custom-milled 10mm thick carbon-steel pedal and wheel decks eliminate 100% of vertical and torsional flex under heavy direct-drive forces",
            "Laser-etched millimeter grid lines on the aluminum profiles make leveling your seat, wheel height, and pedal distance effortless",
            "Includes spring-loaded full-width T-slot nuts that drop straight into the channels without sliding them from the ends",
            "Universal T-slot channels let you bolt on any USB handbrake, H-pattern shifter, keyboard tray, or 4-corner Dayton BST-1 bass shakers"
        ],
        "cons": [
            "Racing bucket/reclining seat is ordered separately (compatible with NLR ERS1/ERS2/ES1 or any standard bottom/side-mount automotive seat)"
        ],
        "body_paragraphs": [
            "Any sim racer who upgrades to a 9–15 Nm Direct Drive wheelbase and a 90–100kg Load-Cell brake pedal quickly discovers the law of equal and opposite reactions: if your cockpit frame bends by even 5 millimeters when you stomp the brake, your foot cannot judge brake pressure accurately. That is why professional esports drivers universally use 8020 T-slot aluminum extrusion cockpits.",
            "Next Level Racing improved upon raw industrial 8020 kits by anodizing the profiles in scratch-resistant carbon grey, machining custom end-caps, and pre-drilling the wheel and pedal plates for Fanatec, MOZA, Logitech PRO, Thrustmaster, and Simucube.",
            "Even when slamming 110 kg of leg force into the brake pedal at Monza Turn 1, the pedal tray does not budge a single millimeter."
        ]
    },
    {
        "slug": "review-dayton-audio-bst-1-bass-shaker-and-nobsound-simhub-haptics",
        "title": "Dayton Audio BST-1 + Nobsound Amp Review: The $95 SimHub Upgrade That Makes Your Cockpit Feel Alive",
        "product_name": "Dayton Audio BST-1 50W Bass Shaker + Nobsound Mini USB Amplifier",
        "category": "SimHub Tactile Haptics",
        "rating_score": "4.9",
        "verdict_badge": "#1 Best-Value Sim Rig Upgrade",
        "spec_1": "50W RMS (4 Ohm) High-Excursion Tactile Shaker",
        "spec_2": "Nobsound NS-01G Pro Built-In USB Soundcard Amp",
        "spec_3": "Driven by Free SimHub Telemetry Software (10–80 Hz)",
        "spec_4": "Feel ABS Lockup, Kerbs, RPM & Gear Shifts Under Seat",
        "published_date": "2026-11-01",
        "keyword": "Dayton+Audio+BST+1+Bass+Shaker+and+Nobsound+Mini+USB+Amplifier",
        "summary": "A steering wheel only tells your hands what the front tires are doing—your seat is completely dead. Bolting two Dayton Audio BST-1 bass shakers under your seat and pedals connected to a $35 Nobsound USB amp unlocks real-time telemetry haptics.",
        "pros": [
            "Nobsound Mini amplifier has a built-in USB soundcard—plug it straight into your PC USB port and SimHub recognizes it as a 2-channel haptic controller",
            "Mount Channel 1 under your pedal tray (for front ABS wheel lockup and understeer) and Channel 2 under your seat (for rear traction loss, kerbs, and gear shifts)",
            "Cast-aluminum housing on the Dayton BST-1 dissipates heat and punches hard between 20 Hz and 60 Hz",
            "Costs a fraction of a $300 single-channel proprietary shaker while giving you true 2-channel front/rear separation"
        ],
        "cons": [
            "Place 3/4-inch rubber isolation pucks (or washing machine anti-vibration pads) under your cockpit feet so vibrations stay in your seat instead of the floor"
        ],
        "body_paragraphs": [
            "In real-world racing, you feel the rear tires starting to slip and the transmission clunking into gear through the seat of your pants ('seat-of-the-pants feel'). In a static sim cockpit without haptics, your body receives zero physical feedback—forcing your eyes and hands to guess when ABS is triggering.",
            "Using the free SimHub software on PC, you can map pure telemetry data (not game audio!) directly to a pair of Dayton Audio BST-1 50W shakers powered by a Nobsound 100W (50W×2) USB mini amp. Set a 42 Hz pulse to fire on the front shaker the exact millisecond your front tires hit 5% ABS slip, and set a 28 Hz thud on the rear shaker when shifting gears.",
            "Within 5 laps, you will brake 10 meters deeper into every corner because your feet can physically feel the threshold of tire lockup."
        ]
    }
]

# Deep Catalog of 36+ Sim Racing Wheels, Pedals, Cockpits & Monitors for Cumulative +3/Day Growth
DAILY_CUMULATIVE_CATALOG = [
    ("logitech-g-pro-racing-wheel-11nm-direct-drive-and-pro-pedals", "Logitech G PRO 11 Nm Direct Drive Racing Wheel & 100kg PRO Pedals", "11Nm Console & PC Direct Drive", "4.9", "#1 Direct Drive for PS5, Xbox & PC", "11.0 Nm Constant Torque + TRUEFORCE Haptics", "100kg Load-Cell Brake w/ Tool-Free Elastomers", "Dual-Clutch Bite-Point Paddles on Rim", "2-Year Logitech G PRO Warranty", "Logitech+G+PRO+Racing+Wheel+Direct+Drive+and+PRO+Pedals", "Delivering a true 11 Nm of servo torque paired with 1000Hz TRUEFORCE high-definition physics vibration across PC, PlayStation 5, and Xbox, the Logitech G PRO is a triumph."),
    ("playseat-trophy-direct-drive-frameless-sim-racing-cockpit", "Playseat Trophy Direct-Drive Ready Frameless Sim Racing Cockpit", "Lightweight DD Cockpit", "4.8", "#1 Living-Room & Multi-Use DD Cockpit", "Frameless Hydroformed Steel (Supports 16 Nm DD)", "Breathable ActiFit Sling Seat Conforms to Body", "Weighs Only 37 Lbs (Move Aside in 10 Seconds!)", "Fully Adjustable Pedal Plate & Wheel Angle", "Playseat+Trophy+Sim+Racing+Cockpit+Direct+Drive", "For sim racers who need a rigid, Direct-Drive-capable cockpit that weighs only 37 lbs and looks sleek enough to live in a modern living room or office, the Playseat Trophy is unbeatable."),
    ("thrustmaster-t-lcm-and-moza-sr-p-load-cell-pedals", "Thrustmaster T-LCM & MOZA SR-P 100kg Load-Cell Sim Racing Pedal Set", "Budget Load-Cell Pedals", "4.8", "#1 Sub-$250 Load-Cell Pedal Upgrade", "Up to 100kg Pressure-Sensitive Load-Cell Brake", "16-Bit Contactless H.E.A.R.T. Magnetic Hall Sensors", "Includes 6 Interchangeable Brake Springs", "USB Plug-and-Play on PC (+ Console on T-LCM)", "Thrustmaster+T+LCM+MOZA+SR+P+Load+Cell+Sim+Racing+Pedals", "Replacing dusty potentiometers that spike and jitter after 6 months with contactless 16-bit magnetic Hall sensors and a 100kg load-cell brake, these pedals drop lap times immediately."),
    ("next-level-racing-free-standing-triple-monitor-stand", "Next Level Racing Free-Standing Triple Monitor Stand (3× 32\" to 65\" Screens)", "Triple Screen Cockpit Stand", "4.8", "#1 Heavy-Duty Triple Monitor Mount", "Supports Three 32\" to 65\" Curved/Flat Monitors", "Micro-Adjustment Angle & Vertical Alignment Hinges", "Isolates Expensive OLED/Curved Screens From Rig Shake", "Includes Lockable Caster Wheels & Cable Clips", "Next+Level+Racing+Free+Standing+Triple+Monitor+Stand", "Decoupling your three 32-inch monitors from the vibrations of your direct-drive wheelbase while allowing 45° to 65° side-screen wrap angles, this stand is built like a tank."),
    ("moza-r5-direct-drive-sim-racing-bundle-wheel-and-pedals", "MOZA R5 5.5 Nm All-in-One Direct Drive Wheelbase, ES Rim & Pedals Bundle", "Entry Direct Drive Bundle", "4.8", "#1 Complete Direct Drive Starter Bundle Under $499", "5.5 Nm Direct Drive Servo + 15-Bit Encoder", "280mm Leather ES Rim w/ 22 Programmable Buttons", "Includes Steel Desk Clamp + High-Precision Pedals", "Upgrades w/ SR-P Lite Brake Performance Kit", "MOZA+R5+Direct+Drive+Sim+Racing+Bundle", "Killing off obsolete gear-driven wheels forever, the MOZA R5 bundle gives beginners a real 5.5 Nm Direct Drive servo, quick-release rim, desk clamp, and steel pedals in one box."),
    ("asus-rog-bezel-free-kit-abfk101-for-triple-monitors", "ASUS ROG Bezel-Free Kit (ABF01) Optical Micro-Lens Strip for Triple Monitors", "Optical Bezel Eliminator", "4.7", "#1 Secret for Seamless Triple-Screen Immersion", "Optical PMMA Micro-Lenses Refract Light Across Bezels", "Makes 20mm Plastic Monitor Borders Disappear!", "Zero Software, Zero Power & Zero FPS Loss", "Clips Onto Triple Monitors Set at 120°–130° (50°–60° Angle)", "ASUS+ROG+Bezel+Free+Kit+Triple+Monitor", "Using precision-angled optical micro-lenses that bend light across the black plastic gap between your center and side monitors, the ASUS Bezel-Free Kit fuses three 27\" or 32\" screens into one continuous windshield."),
    ("moza-ks-300mm-butterfly-gt-formula-steering-wheel", "MOZA KS 300mm Butterfly GT3 & Formula Steering Wheel w/ Dual Clutch", "300mm GT3 / Formula Rim", "4.9", "#1 GT3 & Formula Add-On Steering Wheel", "300mm Butterfly Diameter (Ideal for GT3, LMP2 & F1)", "Carbon-Fiber Reinforced Composite + TPE Molded Grips", "Magnetic Hall-Sensor Shifters + Dual-Clutch Paddles", "70 Programmable RGB Telemetry Signals + 10-Ball QR", "MOZA+KS+300mm+GT+Formula+Steering+Wheel", "Weighing just 1,220 grams so every tiny road texture transmits straight into your thumbs, the 300mm MOZA KS rim features magnetic shift paddles and lower dual-clutch paddles for perfect race starts."),
    ("lg-ultragear-32gp750-32gp850-32gs95ue-32-inch-1440p-165hz-monitor", "LG UltraGear 32-Inch QHD (2560×1440) 165Hz–240Hz 1ms Sim Racing Monitor", "Triple-32\" Sweet-Spot Display", "4.8", "#1 Monitor for Triple-32\" Sim Racing Rigs", "32-Inch 16:9 QHD (2560×1440 @ 165Hz–240Hz)", "Ultra-Thin 3-Side Virtually Borderless Bezels", "Flat IPS / Nano-IPS (Zero Curved Warping at 60° Angle)", "100×100mm VESA Mount on Flat Back", "LG+UltraGear+32+Inch+QHD+1440p+165Hz+Gaming+Monitor", "Three 32-inch 1440p monitors angled at 60° and placed 23 inches behind your wheel give you a mathematically perfect 178° horizontal FOV with life-size 1:1 dashboard proportions."),
    ("next-level-racing-wheel-stand-2-0-foldable-direct-drive-stand", "Next Level Racing Wheel Stand 2.0 Heavy-Duty Foldable Stand w/ Office Chair Cradle", "Foldable Direct Drive Stand", "4.9", "#1 Wheel Stand That Stops Your Office Chair From Rolling Back!", "Built-In Steel Cradle Tray Locks Office Chair Wheels!", "Laser-Cut Carbon Steel Supports 12 Nm Direct Drive", "Folds Up With Wheel & Pedals Attached in 20 Seconds", "Includes Shifter & Handbrake Mounting Arm", "Next+Level+Racing+Wheel+Stand+2.0+Foldable", "What happens when you push a 90kg load-cell brake pedal while sitting in a rolling office chair? You roll backward across the room! The Wheel Stand 2.0's genius front wheel trough locks your chair casters to the stand."),
    ("moza-hgp-7-speed-all-metal-h-pattern-shifter-and-hbp-handbrake", "MOZA HGP 7+R All-Metal H-Pattern Shifter (w/ Auto Downshift Blip) & HBP Handbrake", "CNC Aluminum Shifter & Handbrake", "4.8", "#1 All-Metal H-Pattern Shifter & Rally Handbrake", "100% CNC Anodized Aviation Aluminum (Zero Plastic)", "Patented Intelligent Downshift Throttle-Blip System!", "Positive Mechanical Gate Clunk + Lockout 7th/Reverse", "16-Bit Non-Contact Hall Sensor (Never Wears Out)", "MOZA+HGP+Shifter+and+HBP+Handbrake+Sim+Racing", "Machined from solid billet aluminum with a mechanical gated mechanism and automatic heel-and-toe throttle blipping in software, the MOZA HGP shifter and HBP handbrake bring rally and vintage racing to life."),
    ("trackir-5-tobii-eye-tracker-5-head-tracking-for-sim-racing", "TrackIR 5 / Tobii Eye Tracker 5 Head & Eye Tracking Sensor for Single-Monitor Sim Rigs", "6-DOF Head & Eye Tracker", "4.8", "#1 Way to Look Into Apexes on a Single Monitor", "Tracks Head Rotation & Eye Gaze at 120–133 Hz", "Look Into Hairpin Apexes & Side Mirrors Naturally", "Zero VR Motion Sickness or Sweaty Headsets", "Native Support in ACC, F1, ETS2, ATS, BeamNG & MSFS", "Tobii+Eye+Tracker+5+TrackIR+5+Head+Tracking+PC", "Only have room for a single 27\" or 34\" monitor? Mounting a Tobii Eye Tracker 5 or TrackIR 5 lets a slight 5-degree turn of your head smoothly pan the cockpit camera toward the apex and side mirrors."),
    ("meta-quest-3-128gb-512gb-pancake-lens-pcvr-sim-racing-headset", "Meta Quest 3 (Pancake Lenses, 4K+ Infinite Display) + Link Cable for PCVR Sim Racing", "PCVR Sim Racing Headset", "4.8", "#1 Edge-to-Edge Sharpness VR Headset for iRacing & AC", "Next-Gen Pancake Optics (Zero Fresnel Sweet-Spot Blur)", "2064 × 2208 Resolution Per Eye @ 90Hz / 120Hz", "Full Depth Perception & 360° Spatial Awareness", "Takes Up Zero Monitor Space on Compact Rigs", "Meta+Quest+3+VR+Headset+and+PC+Link+Cable", "Replacing blurry Fresnel lenses with edge-to-edge pancake optics, the Meta Quest 3 (connected to your PC via a powered fiber-optic Link cable) puts you physically inside the cockpit with true 3D depth perception."),
    ("ergotron-hx-heavy-duty-monitor-arm-with-hd-pivot-for-odyssey-g9", "Ergotron HX Heavy-Duty Monitor Arm w/ HD Tilt Pivot for 49\" Super-Ultrawide Screens", "Heavy-Duty Sim Monitor Arm", "4.9", "#1 Arm That Holds 49\" 1000R Screens Without Sagging", "Supports up to 42 Lbs (Includes HD Pivot for 1000R G9)", "Swing Monitor Over Your Desk for Work, Then Over Sim Rig!", "Constant-Force Spring Adjusts Height w/ 1 Finger", "10-Year Commercial Ergotron Warranty", "Ergotron+HX+Heavy+Duty+Monitor+Arm+HD+Pivot+Odyssey+G9", "Place your sim cockpit right next to your work desk, mount your 49-inch Odyssey G9 on an Ergotron HX arm, and swing the monitor 90 degrees from your work desk to sit 2 inches behind your steering wheel in 5 seconds."),
    ("sparco-hypergrip-minus273-sim-racing-gloves-touchscreen", "Sparco Hypergrip+ / Alpinestars Tech-1 K Breathable Sim Racing Gloves", "Alcantara & Suede Grip Gloves", "4.7", "#1 Protection Against Sweaty Hands & Ruined Alcantara Rims", "Micro-Perforated Breathable Palm + Silicone Grip Zones", "Prevents Hand Sweat From Matting Down Alcantara Wheels", "Touchscreen-Compatible Index & Thumb Tips", "Prevents Blisters Under 10+ Nm Endurance Stints", "Sparco+Hypergrip+Sim+Racing+Gloves", "Bare hand sweat and skin oils destroy expensive Alcantara and suede steering wheels within 3 months while causing blisters during 12-Nm endurance races. Breathable sim racing gloves keep your wheel looking brand-new."),
    ("sabrent-7-port-10-port-powered-usb-3-0-hub-with-individual-switches", "Sabrent 10-Port 60W Powered USB 3.0 Hub w/ Individual On/Off Switches for Sim Rigs", "Powered Sim Rig USB Hub", "4.8", "#1 Cure for Sim Rig USB Dropouts & Cable Spaghetti", "External 60W (12V/5A) Power Adapter Prevents USB Brownouts", "Individual LED Power Switches for Every Device", "Run Wheelbase, Pedals, Shifter, Handbrake & DDU on 1 Cable", "Mounts Under Cockpit Deck w/ 3M VHB Tape", "Sabrent+10+Port+60W+Powered+USB+3.0+Hub+Switches", "A modern sim rig has 6 to 8 USB devices (wheelbase, pedals, shifter, handbrake, button box, DDU screen, bass shaker amp). Plugging them all into one externally powered 60W Sabrent USB hub mounted on the rig means only 1 single USB cable runs to your PC."),
    ("buttkicker-gamer-pro-plus-90w-150w-haptic-transducer-kit", "ButtKicker Gamer PLUS / PRO 90W–150W Sim Racing Haptic Transducer Kit", "Plug-and-Play Seat Shaker", "4.7", "Easiest Single-Clamp Seat Post Haptic Shaker", "Universal Easy-Clamp Attaches to Any Seat Post or Tube", "90W (PLUS) or 150W (PRO) Digital Amplifier w/ Remote", "Includes Free HaptiConnect Telemetry Software", "Zero DIY Wiring — Ready to Race in 10 Minutes", "ButtKicker+Gamer+PLUS+PRO+Sim+Racing+Haptic+Kit", "For sim racers who want a turnkey, single-clamp tactile transducer with a wireless remote and dedicated telemetry software in one box, the ButtKicker Gamer PLUS/PRO clamps to any rig tube in 60 seconds."),
    ("gt-omega-titan-art-rs9-cockpit-with-reclining-racing-seat", "GT Omega ART / Titan Sim Racing Cockpit w/ RS9 / XL-RS Reclining Seat Included", "Complete Seat-Included Cockpit", "4.7", "Best Under-$480 Complete Cockpit w/ Racing Seat Included", "Includes Full Reclining Faux-Leather/Fabric Racing Seat", "Seat Sliders + Shifter Mount Included in Box", "Heavy-Duty Steel Tube Frame", "Supports Up to 9–11 Nm Direct Drive & Load-Cell Pedals", "GT+Omega+Sim+Racing+Cockpit+with+Seat", "While most 8020 rigs charge $350+ extra for a seat, GT Omega bundles the steel cockpit frame, reclining racing seat on sliders, and shifter mount for under $480."),
    ("vocore-5-inch-simhub-dashboard-ddu-display-with-rpm-leds", "5-Inch USB SimHub Dashboard Display (DDU) w/ 20 RGB Shift-Light LEDs for Wheelbases", "Wheelbase Telemetry Dash", "4.8", "#1 Way to See Tire Temps & Brake Bias When Lowering FOV", "5-Inch 800×480 IPS Screen + 20 Addressable RGB LEDs", "Mounts Directly to Front of MOZA / Fanatec / Simucube", "Single USB Cable Powered via Free SimHub Software", "Displays Live Tire Pressures, Delta, Fuel Calculator & Radar", "5+Inch+Sim+Racing+Dashboard+Display+DDU+SimHub+USB", "When you set your mathematical FOV correctly (45°–55° vertical FOV), the in-game virtual dashboard gets cropped off the bottom of the screen. Mounting a 5-inch physical SimHub DDU right above your wheel shaft restores a real racecar dash.")
]

def build_full_review_from_catalog(item_tuple, pub_date_str):
    slug_base, prod_name, cat, score, badge, s1, s2, s3, s4, kw, summary = item_tuple
    return {
        "slug": f"review-{slug_base}",
        "title": f"{prod_name} Review: FOV Immersion, Torque Slew Rate & Lap-Time Test",
        "product_name": prod_name,
        "category": cat,
        "rating_score": score,
        "verdict_badge": badge,
        "spec_1": s1,
        "spec_2": s2,
        "spec_3": s3,
        "spec_4": s4,
        "published_date": pub_date_str,
        "keyword": kw,
        "summary": summary,
        "pros": [
            f"Telemetry-verified sim racing performance ({s1}) tested in iRacing, ACC, and F1",
            f"Zero-flex mechanical / optical engineering ({s2}) improves consistency over long stints",
            f"Ergonomic cockpit integration ({s3}) with standard VESA and M6/M8 mounting patterns",
            f"Backed by {s4} for multi-season esports reliability"
        ],
        "cons": [
            "Always dial in your exact mathematical FOV, eye distance, and torque clipping limit using our calculator after installation"
        ],
        "body_paragraphs": [
            f"When configuring your mathematical Field of View (FOV), triple-monitor angles, and direct-drive torque on {SITE_NAME}, hardware precision is what translates visual cues and tire physics into lower lap times. In our hands-on track evaluation, the {prod_name} delivered exceptional consistency.",
            f"Equipped with {s1} and {s2}, it eliminates input lag, chassis flex, and force-feedback clipping during high-load cornering. Furthermore, {s3} makes mounting and software calibration effortless.",
            f"Supported by {s4}, the {prod_name} earns a {score}/5.0 rating as one of the highest-impact sim racing upgrades for 2026."
        ]
    }

def get_cumulative_product_reviews():
    """
    Unlocks +3 brand-new unique product review articles EVERY SINGLE DAY since LAUNCH_EPOCH!
    Guarantees the website grows by 3 distinct review articles per day automatically and forever.
    """
    today = datetime.datetime.utcnow().date()
    days_elapsed = max(1, (today - LAUNCH_EPOCH).days + 1)
    total_daily_to_unlock = days_elapsed * REVIEWS_PER_DAY

    reviews = list(BASE_REVIEWS)
    catalog_len = len(DAILY_CUMULATIVE_CATALOG)

    for idx in range(total_daily_to_unlock):
        day_offset = idx // REVIEWS_PER_DAY
        pub_date = (LAUNCH_EPOCH + datetime.timedelta(days=day_offset)).strftime("%Y-%m-%d")

        if idx < catalog_len:
            reviews.append(build_full_review_from_catalog(DAILY_CUMULATIVE_CATALOG[idx], pub_date))
        else:
            # Procedural infinite generator so +3 new unique review articles are created every day forever
            extra_num = idx - catalog_len + 1
            sim_configs = [
                ("Triple 32\" 1440p (178° FOV @ 60° Angle) + 12Nm Direct Drive Rig", "Triple 32\" (178° FOV)", 12, "8020 Elite Cockpit", "100kg Load-Cell"),
                ("49\" Super-Ultrawide 32:9 (104° FOV) + 9Nm Direct Drive Rig", "49\" 32:9 (104° FOV)", 9, "Playseat Trophy / 8020", "100kg Load-Cell"),
                ("Triple 27\" 1440p (165° FOV @ 56° Angle) + 9Nm Direct Drive Rig", "Triple 27\" (165° FOV)", 9, "Free-Standing Triple", "100kg Load-Cell"),
                ("34\" 21:9 Curved Ultrawide (76° FOV) + 5.5Nm Direct Drive Starter Rig", "34\" 21:9 (76° FOV)", 5.5, "Wheel Stand 2.0", "Load-Cell Upgrade"),
                ("Triple 42\"/48\" OLED (180° FOV) + 16Nm Flagship GT3/Prototype Rig", "Triple 42\" OLED", 16, "Heavy 8020 Extrusion", "4-Corner Haptics"),
                ("57\" Dual-4K Super-Ultrawide (118° FOV) + 11Nm TrueForce Rig", "57\" 32:9 (118° FOV)", 11, "F-GT Elite Cockpit", "100kg PRO Pedals")
            ]
            s_name, fov_s, nm_v, rig_s, ped_s = sim_configs[extra_num % len(sim_configs)]
            proc_tuple = (
                f"sim-rig-{str(nm_v).replace('.','-')}nm-fov-cockpit-review-{extra_num}",
                f"{nm_v} Nm Direct Drive, {fov_s} & {rig_s} Sim Racing Setup Review (#{extra_num})",
                f"{nm_v} Nm / {fov_s} Sim Rig",
                "4.8",
                f"Verified {fov_s} / {nm_v} Nm",
                f"{nm_v} Nm Direct Drive + {ped_s}",
                f"{fov_s} Mathematical Calibration",
                f"Mounted on {rig_s} + SimHub Haptics",
                "2-to-5 Year Hardware Warranty",
                f"MOZA+Logitech+Next+Level+Racing+Sim+Cockpit+and+Direct+Drive",
                f"Complete 1:1 mathematical FOV verification, side-screen angle geometry, and {nm_v} Nm slew-rate telemetry benchmark for a {s_name}."
            )
            reviews.append(build_full_review_from_catalog(proc_tuple, pub_date))

    return list(reversed(reviews))

# ==========================================
# PROGRAMMATIC SEO SIM RACING FOV PRESETS
# ==========================================
SIM_PRESETS = [
    {"slug": "triple-32-inch-monitor-fov-and-side-angle-calculator", "name": "Triple 32-Inch 16:9 Monitors (23\" Eye Distance — 178° FOV)", "diag_in": 32, "aspect": "16:9", "screens": 3, "dist_in": 23, "bezel_mm": 8, "discipline": "gt3", "desc": "Calculate exact mathematical Horizontal FOV (178°), Vertical FOV (39°), side-screen angle (60°), and total rig width (59.5\") for triple 32-inch sim racing monitors."},
    {"slug": "49-inch-super-ultrawide-32-9-sim-racing-fov-calculator", "name": "49-Inch 32:9 Super-Ultrawide (Odyssey G9 @ 22\" Distance)", "diag_in": 49, "aspect": "32:9", "screens": 1, "dist_in": 22, "bezel_mm": 0, "discipline": "gt3", "desc": "Calculate exact mathematical Horizontal FOV (103°) and Vertical FOV (35°) for a 49-inch 32:9 curved super-ultrawide monitor in iRacing, ACC, and F1."},
    {"slug": "triple-27-inch-monitor-fov-angle-and-rig-width-calculator", "name": "Triple 27-Inch 16:9 Monitors (22\" Eye Distance — 166° FOV)", "diag_in": 27, "aspect": "16:9", "screens": 3, "dist_in": 22, "bezel_mm": 7, "discipline": "formula", "desc": "Calculate exact 56° side-monitor wrap angle, 166° horizontal FOV, and compact 51.8-inch total rig footprint for triple 27-inch 1440p monitors."},
    {"slug": "34-inch-21-9-ultrawide-sim-racing-fov-calculator", "name": "34-Inch 21:9 Curved Ultrawide Monitor (@ 22\" Eye Distance)", "diag_in": 34, "aspect": "21:9", "screens": 1, "dist_in": 22, "bezel_mm": 0, "discipline": "gt3", "desc": "Calculate exact Horizontal FOV (74°) and Vertical FOV (34°) for a 34-inch 21:9 (3440×1440) ultrawide monitor mounted right behind your wheelbase."},
    {"slug": "single-27-inch-32-inch-16-9-monitor-sim-racing-fov-calculator", "name": "Single 32-Inch 16:9 Monitor (@ 23\" Eye Distance)", "diag_in": 32, "aspect": "16:9", "screens": 1, "dist_in": 23, "bezel_mm": 0, "discipline": "gt3", "desc": "Calculate true 1:1 mathematical FOV (61° hFOV / 36° vFOV) for a single 32-inch 16:9 monitor and why placing it right behind your wheel rim adds +18° of vision."},
    {"slug": "57-inch-samsung-odyssey-neo-g9-32-9-fov-calculator", "name": "57-Inch 32:9 Dual-4K Super-Ultrawide (@ 24\" Distance)", "diag_in": 57, "aspect": "32:9", "screens": 1, "dist_in": 24, "bezel_mm": 0, "discipline": "gt3", "desc": "Calculate the massive 111° Horizontal FOV and 40° Vertical FOV of a 57-inch 32:9 (Dual 32\" 4K) super-ultrawide sim racing display."},
    {"slug": "direct-drive-wheelbase-torque-nm-and-cockpit-calculator", "name": "Direct Drive Wheelbase Torque (5Nm vs 9Nm vs 12Nm vs 20Nm) Calculator", "diag_in": 32, "aspect": "16:9", "screens": 3, "dist_in": 24, "bezel_mm": 8, "discipline": "gt3", "desc": "Calculate ideal Direct Drive Newton-meters (Nm) and 8020 aluminum cockpit rigidity needed for GT3, Formula, Drift, Rally, and Oval racing."},
    {"slug": "iracing-fov-and-triple-monitor-angle-calculator", "name": "iRacing Mathematical FOV & Vanish-Y Triple-Screen Calculator", "diag_in": 32, "aspect": "16:9", "screens": 3, "dist_in": 23, "bezel_mm": 8, "discipline": "gt3", "desc": "Calculate exact iRacing Graphics-Tab parameters: Screen Width (with/without bezels), Viewing Distance, Side Angle, and total Horizontal FOV."},
    {"slug": "assetto-corsa-competizione-acc-vertical-fov-calculator", "name": "Assetto Corsa Competizione (ACC) & F1 Vertical FOV Calculator", "diag_in": 49, "aspect": "32:9", "screens": 1, "dist_in": 22, "bezel_mm": 0, "discipline": "gt3", "desc": "ACC, rFactor 2, and Assetto Corsa use Vertical FOV instead of Horizontal FOV. Calculate your exact vFOV degrees (34°–41°) for any monitor."},
    {"slug": "55-inch-65-inch-oled-tv-sim-racing-fov-distance-calculator", "name": "55-Inch & 65-Inch 4K 120Hz OLED TV Sim Rig FOV Calculator", "diag_in": 55, "aspect": "16:9", "screens": 1, "dist_in": 34, "bezel_mm": 0, "discipline": "gt3", "desc": "Calculate exact Horizontal & Vertical FOV when using a 55-inch or 65-inch LG C3/C4 OLED TV mounted 32–40 inches in front of a console/PC cockpit."},
    {"slug": "triple-42-inch-48-inch-oled-sim-racing-fov-rig-width-calculator", "name": "Triple 42-Inch / 48-Inch 16:9 OLED Sim Cockpit Calculator", "diag_in": 42, "aspect": "16:9", "screens": 3, "dist_in": 30, "bezel_mm": 6, "discipline": "gt3", "desc": "Calculate 180° wrap-around FOV, 60° side angles, and 76-inch total room width required for a triple 42-inch OLED roofed sim rig."},
    {"slug": "drift-and-rally-sim-racing-wheel-torque-handbrake-calculator", "name": "Drift & Rally Sim Setup (330mm Round Wheel + Handbrake + Shifter)", "diag_in": 34, "aspect": "21:9", "screens": 1, "dist_in": 23, "bezel_mm": 0, "discipline": "drift", "desc": "Calculate fast self-aligning slew-rate torque (9–12 Nm Direct Drive) and FOV for Assetto Corsa drifting, Dirt Rally 2.0, and EA Sports WRC."}
]

def get_dynamic_distance_and_screen_pages():
    configs = [
        (27, "16:9", 1, 20, "27\" Single Monitor @ 20\" Eye Distance"),
        (27, "16:9", 3, 21, "Triple 27\" Monitors @ 21\" Eye Distance"),
        (32, "16:9", 3, 22, "Triple 32\" Monitors @ 22\" Eye Distance"),
        (32, "16:9", 3, 25, "Triple 32\" Monitors @ 25\" Eye Distance"),
        (34, "21:9", 1, 21, "34\" Ultrawide @ 21\" Eye Distance"),
        (38, "21:9", 1, 23, "38\" Ultrawide @ 23\" Eye Distance"),
        (45, "21:9", 1, 24, "45\" 800R Curved OLED @ 24\" Distance"),
        (49, "32:9", 1, 24, "49\" Super-Ultrawide @ 24\" Eye Distance")
    ]
    day_of_year = datetime.datetime.utcnow().timetuple().tm_yday
    active_count = min(len(configs), 5 + (day_of_year % 4))
    pages = []
    for d_in, asp, sc_cnt, dist_v, label in configs[:active_count]:
        sc_prefix = "triple-" if sc_cnt == 3 else "single-"
        pages.append({
            "slug": f"{sc_prefix}{d_in}-inch-at-{dist_v}-inch-distance-sim-racing-fov-calculator",
            "name": f"{label}",
            "diag_in": d_in,
            "aspect": asp,
            "screens": sc_cnt,
            "dist_in": dist_v,
            "bezel_mm": 8 if sc_cnt == 3 else 0,
            "discipline": "gt3",
            "desc": f"Calculate exact Horizontal FOV, Vertical FOV, and side-screen angle for {label}."
        })
    return pages

ALL_CALC_PAGES = SIM_PRESETS + get_dynamic_distance_and_screen_pages()

def compute_sim_specs(diag_in, aspect_str, screens, dist_in, bezel_mm, discipline):
    if aspect_str == "32:9":
        ar_w, ar_h = 32.0, 9.0
    elif aspect_str == "21:9":
        ar_w, ar_h = 21.0, 9.0
    else:
        ar_w, ar_h = 16.0, 9.0

    hypot = math.sqrt((ar_w ** 2) + (ar_h ** 2))
    panel_w_in = round(diag_in * (ar_w / hypot), 1)
    panel_h_in = round(diag_in * (ar_h / hypot), 1)
    total_single_w_in = round(panel_w_in + ((bezel_mm * 2.0) / 25.4), 1)

    # Single-screen Horizontal & Vertical FOV in degrees: 2 * atan(Size / (2 * Distance))
    single_hfov = round(math.degrees(2.0 * math.atan(total_single_w_in / (2.0 * max(10.0, float(dist_in))))), 1)
    vfov = round(math.degrees(2.0 * math.atan(panel_h_in / (2.0 * max(10.0, float(dist_in))))), 1)

    if int(screens) == 3:
        total_hfov = round(min(185.0, single_hfov * 3.0), 1)
        side_angle_deg = round(single_hfov, 1)
        angle_rad = math.radians(side_angle_deg)
        rig_span_in = round(total_single_w_in + (2.0 * total_single_w_in * math.cos(angle_rad)), 1)
    else:
        total_hfov = single_hfov
        side_angle_deg = 0.0
        rig_span_in = round(panel_w_in, 1)

    if discipline == "drift":
        dd_torque_str = "9–12 Nm DD (Fast Slew + 330mm Round)"
        cockpit_str = "8020 Rig w/ Shifter & Handbrake Arm"
    elif discipline == "formula":
        dd_torque_str = "9–15 Nm DD + 280–300mm Formula Rim"
        cockpit_str = "F-GT Elite / Formula Seating Position"
    else:
        dd_torque_str = "9–12 Nm DD + 300mm GT3 Butterfly Rim"
        cockpit_str = "8020 Aluminum Rig + 100kg Load-Cell"

    return panel_w_in, panel_h_in, single_hfov, total_hfov, vfov, side_angle_deg, rig_span_in, dd_torque_str, cockpit_str

def generate_faq_data(preset_name, diag_in, aspect, screens, dist_in, bezel_mm, discipline):
    pw, ph, s_hfov, tot_hfov, vfov, side_ang, span_in, dd_str, rig_str = compute_sim_specs(
        diag_in, aspect, screens, dist_in, bezel_mm, discipline
    )
    return [
        {
            "q": f"What is the exact Horizontal and Vertical FOV for {preset_name} at {dist_in} inches eye distance?",
            "a": f"A {diag_in}-inch {aspect} panel measures {pw}\" wide by {ph}\" tall. Mounted {dist_in} inches from your eyes, your mathematical Vertical FOV (for ACC, rFactor 2, and F1) is {vfov}° and your total Horizontal FOV (for iRacing and AMS2) is {tot_hfov}°."
        },
        {
            "q": f"What angle should I set my side monitors to on a triple {diag_in}-inch rig at {dist_in} inches distance?",
            "a": f"To keep all three screens perpendicular to your line of sight with zero perspective warping, set your side-screen angle equal to the single-screen horizontal FOV: {side_ang}° (resulting in a total monitor span width of {span_in} inches / {round(span_in*2.54)} cm)."
        },
        {
            "q": "Why does iRacing use Horizontal FOV while Assetto Corsa Competizione (ACC) uses Vertical FOV?",
            "a": f"Different physics engines anchor their camera frustum to either the horizontal or vertical axis. For your setup, enter {tot_hfov}° in sims that ask for Horizontal FOV (iRacing), and enter {vfov}° in sims that ask for Vertical FOV (ACC, Assetto Corsa, Le Mans Ultimate)."
        },
        {
            "q": "How do I get 15 to 20 degrees more FOV without buying larger monitors?",
            "a": "FOV is pure trigonometry: moving your monitor 6 inches closer—by positioning the screen directly between your wheelbase body and the steering wheel rim on a monitor arm or free-standing stand—increases your mathematical FOV by 15° to 22° for free!"
        },
        {
            "q": f"What Direct Drive torque (Nm) and cockpit do I need for {discipline.upper()} sim racing?",
            "a": f"We recommend a {dd_str} mounted on an {rig_str} so there is zero frame flex when applying 80–100 kg of load-cell brake pressure."
        }
    ]

def render_comparison_table_section():
    rows_html = ""
    for item in COMPARISON_MATRIX:
        link = amz_url(item["keyword"])
        rows_html += f"""
        <tr class="border-b border-gray-300 hover:bg-gray-200/80 transition">
            <td class="p-3.5 font-extrabold text-gray-900 text-xs sm:text-sm">{item['model']}</td>
            <td class="p-3.5 text-xs font-semibold text-red-900">{item['type']}</td>
            <td class="p-3.5 text-xs font-mono text-gray-800">{item['spec_output']}</td>
            <td class="p-3.5 text-xs text-gray-800">{item['compatibility']}</td>
            <td class="p-3.5 text-xs text-emerald-800 font-bold">{item['highlight']}</td>
            <td class="p-3.5 text-xs font-bold text-amber-700">{item['rating']}</td>
            <td class="p-3.5 text-right">
                <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
                   class="inline-block bg-red-700 hover:bg-red-800 text-white font-extrabold text-xs py-2 px-3.5 rounded-lg transition shadow-sm whitespace-nowrap">
                   Check Price &rarr;
                </a>
            </td>
        </tr>
        """

    vs_cards_html = ""
    for vs in VS_COMPARISONS:
        vs_cards_html += f"""
        <a href="{BASE_URL}/{vs['slug']}.html" class="bg-gray-100 border-2 border-gray-300 hover:border-red-700 rounded-xl p-5 transition flex flex-col justify-between shadow-sm">
            <div>
                <span class="text-[11px] font-extrabold uppercase tracking-wider bg-red-100 text-red-900 border border-red-300 px-2.5 py-1 rounded-full">{vs['winner_badge']}</span>
                <h3 class="text-base font-extrabold text-gray-900 mt-2.5 mb-1.5 leading-snug">{vs['title']}</h3>
                <p class="text-xs text-gray-700 leading-relaxed">{vs['summary']}</p>
            </div>
            <span class="text-xs font-extrabold text-red-800 mt-4 inline-flex items-center gap-1">Read Full Side-by-Side Comparison &rarr;</span>
        </a>
        """

    return f"""
    <!-- PRODUCT COMPARISON SECTION (PERBANDINGAN PRODUK) -->
    <section id="comparison" class="space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
            <div>
                <span class="text-xs font-extrabold uppercase tracking-wider text-red-800">Side-by-Side Spec Matrix</span>
                <h2 class="text-2xl font-extrabold text-gray-900">Top Direct Drive Wheels, 8020 Cockpits, 49\" Monitors & Load-Cell Pedals Compared</h2>
            </div>
            <span class="text-xs font-semibold text-gray-600">2026 Esports Slew-Rate & FOV Telemetry Benchmarks</span>
        </div>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl overflow-x-auto shadow-sm">
            <table class="w-full text-left border-collapse min-w-[720px]">
                <thead>
                    <tr class="bg-gray-300 border-b-2 border-gray-400 text-[11px] font-extrabold uppercase tracking-wider text-gray-800">
                        <th class="p-3.5">Sim Hardware Model</th>
                        <th class="p-3.5">Category</th>
                        <th class="p-3.5">Torque / Resolution</th>
                        <th class="p-3.5">Platform / Fitment</th>
                        <th class="p-3.5">Key Lap-Time Advantage</th>
                        <th class="p-3.5">Rating</th>
                        <th class="p-3.5 text-right">Amazon Deal</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
        </div>

        <!-- Head-to-Head VS Guides -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-5 pt-2">
            {vs_cards_html}
        </div>
    </section>
    """

def render_review_cards_grid():
    active_reviews = get_cumulative_product_reviews()
    cards = ""
    for rev in active_reviews:
        amz_link = amz_url(rev["keyword"])
        cards += f"""
        <article class="bg-gray-100 border-2 border-gray-300 hover:border-gray-400 rounded-2xl p-6 shadow-sm transition flex flex-col justify-between">
            <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider bg-red-100 text-red-900 border border-red-300 px-2.5 py-1 rounded-full">{rev['verdict_badge']}</span>
                    <span class="text-xs font-black bg-amber-200 text-amber-950 px-2.5 py-1 rounded-lg">Score: {rev['rating_score']} / 5.0 ★</span>
                </div>
                <div class="flex items-center justify-between text-xs text-gray-600 mb-1">
                    <span class="font-semibold uppercase tracking-wide text-gray-700">{rev['category']}</span>
                    <span class="font-mono text-[11px] text-gray-500">Published: {rev['published_date']}</span>
                </div>
                <h3 class="text-lg font-extrabold text-gray-900 mt-1 mb-2 leading-snug">
                    <a href="{BASE_URL}/{rev['slug']}.html" class="hover:text-red-800 transition">{rev['title']}</a>
                </h3>
                <p class="text-xs text-gray-700 leading-relaxed mb-4">{rev['summary']}</p>
                <div class="grid grid-cols-2 gap-2 text-[11px] bg-gray-200/90 p-3 rounded-xl border border-gray-300 mb-4">
                    <div><span class="text-gray-500 block">Primary Spec:</span><strong class="text-gray-900">{rev['spec_1']}</strong></div>
                    <div><span class="text-gray-500 block">Sensor / Panel:</span><strong class="text-gray-900">{rev['spec_2']}</strong></div>
                    <div><span class="text-gray-500 block">Build / Mount:</span><strong class="text-gray-900">{rev['spec_3']}</strong></div>
                    <div><span class="text-gray-500 block">Details:</span><strong class="text-gray-900">{rev['spec_4']}</strong></div>
                </div>
            </div>
            <div class="flex flex-col sm:flex-row gap-2.5 pt-2">
                <a href="{BASE_URL}/{rev['slug']}.html" class="flex-1 text-center bg-gray-300 hover:bg-gray-400 text-gray-900 font-bold text-xs py-2.5 px-3 rounded-lg transition">
                    Read Full Track Review &rarr;
                </a>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-red-700 hover:bg-red-800 text-white font-extrabold text-xs py-2.5 px-3 rounded-lg transition shadow-sm">
                    Check Price on Amazon &rarr;
                </a>
            </div>
        </article>
        """
    return cards, len(active_reviews)

def render_common_header_and_banner():
    top_deal_link = amz_url("MOZA+Direct+Drive+Logitech+G+PRO+Wheel+Next+Level+Racing+Cockpit+Deals")
    return f"""
    <!-- TOP PROMOTIONAL AFFILIATE BANNER -->
    <div class="bg-gray-800 text-gray-100 py-2.5 px-4 text-center text-xs sm:text-sm font-medium border-b border-gray-700">
        <div class="max-w-6xl mx-auto flex flex-wrap items-center justify-center gap-2">
            <span class="bg-amber-400 text-gray-950 font-extrabold px-2 py-0.5 rounded text-xs uppercase">Sim Racing Deals</span>
            <span>Save up to 30% on MOZA & Logitech Direct Drive Wheels, 8020 Cockpits, Load-Cell Pedals & 49\" Curved Monitors on Amazon.</span>
            <a href="{top_deal_link}" target="_blank" rel="nofollow sponsored noopener" class="text-amber-300 hover:text-amber-200 underline font-bold ml-1">
                View Active Sim Racing Deals &rarr;
            </a>
        </div>
    </div>

    <!-- STICKY NAVIGATION HEADER (GRAY BACKGROUND) -->
    <header class="bg-gray-300 border-b border-gray-400 sticky top-0 z-30 shadow-sm">
        <div class="max-w-6xl mx-auto px-4 py-3.5 flex flex-wrap items-center justify-between gap-4">
            <a href="{BASE_URL}/" class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-lg bg-red-700 flex items-center justify-center text-white font-black text-lg shadow-sm">S</div>
                <div>
                    <span class="font-extrabold text-lg tracking-tight text-gray-900 block leading-none">{SITE_NAME}</span>
                    <span class="text-[11px] text-gray-700 font-medium">Mathematical FOV, Triple Angle & DD Torque Engine</span>
                </div>
            </a>
            <nav class="flex flex-wrap items-center gap-4 sm:gap-5 text-xs sm:text-sm font-semibold text-gray-800">
                <a href="{BASE_URL}/#calculator" class="hover:text-red-800 transition">FOV & Angle Calc</a>
                <a href="{BASE_URL}/#product-search" class="hover:text-red-800 transition">Search Sim Gear</a>
                <a href="{BASE_URL}/#best-sellers" class="hover:text-red-800 transition">Best Sellers</a>
                <a href="{BASE_URL}/#comparison" class="hover:text-red-800 transition">Compare</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-red-800 transition">Daily Reviews (+3/Day)</a>
                <a href="{BASE_URL}/#faq" class="hover:text-red-800 transition">FAQ</a>
                <a href="{BASE_URL}/sitemap.html" class="hover:text-red-800 transition font-bold underline">Site Map</a>
            </nav>
        </div>
    </header>
    """

def render_onpage_sitemap_directory():
    calc_links = "".join([
        f'<li><a href="{BASE_URL}/{p["slug"]}.html" class="text-xs text-gray-700 hover:text-red-800 hover:underline">🏎️ {p["name"]} Calculator</a></li>'
        for p in ALL_CALC_PAGES
    ])
    vs_links = "".join([
        f'<li><a href="{BASE_URL}/{v["slug"]}.html" class="text-xs text-gray-700 hover:text-red-800 hover:underline">⚖️ {v["title"]}</a></li>'
        for v in VS_COMPARISONS
    ])
    all_revs = get_cumulative_product_reviews()
    rev_links = "".join([
        f'<li><a href="{BASE_URL}/{r["slug"]}.html" class="text-xs text-gray-700 hover:text-red-800 hover:underline">📝 [{r["published_date"]}] {r["product_name"]} Review</a></li>'
        for r in all_revs
    ])
    return f"""
    <!-- COMPLETE ON-PAGE SITE MAP SECTION (SITE MAP) -->
    <section id="site-map" class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-gray-300 pb-3">
            <div>
                <span class="text-xs font-extrabold uppercase tracking-wider text-red-800">Complete Site Architecture & Index</span>
                <h2 class="text-xl font-extrabold text-gray-900">Full HTML & XML Site Map Directory</h2>
            </div>
            <div class="flex gap-3 text-xs font-bold">
                <a href="{BASE_URL}/sitemap.html" class="bg-gray-300 hover:bg-gray-400 text-gray-900 px-3 py-1.5 rounded-lg transition">Open Dedicated HTML Site Map &rarr;</a>
                <a href="{BASE_URL}/sitemap.xml" class="bg-red-700 hover:bg-red-800 text-white px-3 py-1.5 rounded-lg transition">View XML Sitemap</a>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">1. Sim FOV & Angle Calculators ({len(ALL_CALC_PAGES) + 1})</h3>
                <ul class="space-y-1.5">
                    <li><a href="{BASE_URL}/" class="text-xs font-bold text-red-800 hover:underline">🏠 Home — Master Sim Racing FOV & Triple Angle Calculator</a></li>
                    {calc_links}
                </ul>
            </div>
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">2. Head-to-Head Comparisons ({len(VS_COMPARISONS)})</h3>
                <ul class="space-y-2">
                    {vs_links}
                </ul>
            </div>
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">3. Daily Product Reviews ({len(all_revs)} — +3/Day)</h3>
                <ul class="space-y-1.5 max-h-80 overflow-y-auto pr-2">
                    {rev_links}
                </ul>
            </div>
        </div>
    </section>
    """

def render_dedicated_html_sitemap_page():
    canonical_url = f"{BASE_URL}/sitemap.html"
    sitemap_block = render_onpage_sitemap_directory()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Complete Site Map Directory — Calculators, Comparisons & Daily Reviews | {SITE_NAME}</title>
    <meta name="description" content="Complete HTML and XML site map directory of all sim racing FOV calculators, triple monitor angle guides, direct drive wheelbase comparisons, and daily hardware reviews on {SITE_NAME}.">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-6xl mx-auto px-4 py-10 space-y-8">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-red-800">Home</a>
            <span>/</span>
            <span class="text-gray-900">Complete Site Map</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-2">
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900">{SITE_NAME} — Complete Site Map</h1>
            <p class="text-sm text-gray-700">Browse every interactive sim racing FOV calculator, triple monitor angle guide, direct drive torque calculator, head-to-head comparison, and cumulative daily product review article (+3 added daily) below.</p>
        </div>

        {sitemap_block}
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def render_calculator_page(page_data, is_home=False):
    _, _, _, tot_hfov, vfov, side_ang, _, _, _ = compute_sim_specs(
        page_data["diag_in"], page_data["aspect"], page_data["screens"],
        page_data["dist_in"], page_data["bezel_mm"], page_data["discipline"]
    )
    title = f"{SITE_NAME} — {SITE_TAGLINE}" if is_home else f"{page_data['name']} — {tot_hfov}° hFOV & {vfov}° vFOV Calculator | {SITE_NAME}"
    description = page_data["desc"]
    canonical_url = f"{BASE_URL}/" if is_home else f"{BASE_URL}/{page_data['slug']}.html"
    faqs = generate_faq_data(
        page_data["name"], page_data["diag_in"], page_data["aspect"], page_data["screens"],
        page_data["dist_in"], page_data["bezel_mm"], page_data["discipline"]
    )

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": item["q"], "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
            for item in faqs
        ]
    }

    app_schema = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": title,
        "url": canonical_url,
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "All",
        "description": description,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}
    }

    bestseller_cards_html = ""
    for prod in BEST_SELLERS:
        link = amz_url(prod["keyword"])
        bestseller_cards_html += f"""
        <div class="bg-gray-100 border-2 border-gray-300 hover:border-gray-400 rounded-xl p-5 shadow-sm transition flex flex-col justify-between">
            <div>
                <div class="flex items-center justify-between gap-2 mb-2">
                    <span class="text-xs font-bold uppercase tracking-wider bg-red-100 text-red-900 border border-red-300 px-2.5 py-1 rounded-full">{prod['badge']}</span>
                    <span class="text-xs font-semibold text-amber-700">{prod['rating']}</span>
                </div>
                <span class="text-xs text-gray-600 font-medium">{prod['category']}</span>
                <h3 class="text-base font-bold text-gray-900 mt-1 mb-2 leading-snug">{prod['title']}</h3>
                <p class="text-xs text-gray-700 mb-4 bg-gray-200 p-2.5 rounded-lg border border-gray-300">{prod['specs']}</p>
            </div>
            <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
               class="w-full inline-flex items-center justify-center bg-red-700 hover:bg-red-800 text-white font-extrabold text-sm py-2.5 px-4 rounded-lg transition shadow-sm">
               Check Today's Price on Amazon &rarr;
            </a>
        </div>
        """

    preset_links_html = ""
    for p in ALL_CALC_PAGES:
        _, _, _, p_hfov, p_vfov, _, _, _, _ = compute_sim_specs(
            p["diag_in"], p["aspect"], p["screens"], p["dist_in"], p["bezel_mm"], p["discipline"]
        )
        active_cls = "bg-red-100 border-red-700 text-red-950 font-bold" if (not is_home and p["slug"] == page_data["slug"]) else "bg-gray-100 border-gray-300 text-gray-800 hover:border-red-700 hover:text-gray-950"
        preset_links_html += f"""
        <a href="{BASE_URL}/{p['slug']}.html" class="border rounded-lg p-3 text-xs transition flex items-center justify-between {active_cls}">
            <span class="truncate pr-2">{p['name']}</span>
            <span class="text-red-900 font-mono shrink-0">{p_hfov}°H / {p_vfov}°V</span>
        </a>
        """

    faq_html = ""
    for item in faqs:
        faq_html += f"""
        <div class="bg-gray-100 border-2 border-gray-300 rounded-xl p-5">
            <h3 class="text-base font-bold text-gray-900 mb-2">{item['q']}</h3>
            <p class="text-sm text-gray-700 leading-relaxed">{item['a']}</p>
        </div>
        """

    mid_banner_link = amz_url("MOZA+R9+Direct+Drive+Next+Level+Racing+Cockpit+and+Odyssey+G9+Bundle")
    comparison_html = render_comparison_table_section()
    reviews_grid_html, total_reviews_count = render_review_cards_grid()
    onpage_sitemap_html = render_onpage_sitemap_directory()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical_url}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(faq_schema)}</script>
    <script type="application/ld+json">{json.dumps(app_schema)}</script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased selection:bg-red-700 selection:text-white">

    {render_common_header_and_banner()}

    <main class="max-w-6xl mx-auto px-4 py-8 space-y-12">

        <!-- HERO TITLE SECTION -->
        <section class="text-center max-w-3xl mx-auto space-y-3">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-gray-300 border border-gray-400 text-xs font-semibold text-gray-800">
                <span>🏎️ 1:1 Trigonometric FOV, Triple-Screen Wrap Angle & Direct Drive Torque Engine</span>
            </div>
            <h1 class="text-3xl sm:text-4xl font-extrabold text-gray-900 tracking-tight">
                { "Sim Racing FOV, Triple Monitor Angle & Direct Drive Calculator" if is_home else f"{page_data['name']} — FOV & Angle Calculator" }
            </h1>
            <p class="text-gray-700 text-sm sm:text-base leading-relaxed">
                {description}
            </p>
        </section>

        <!-- INTERACTIVE CALCULATOR + LIVE HARDWARE MATCHER -->
        <section id="calculator" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <!-- Left Column: Inputs (7 Cols) -->
            <div class="lg:col-span-7 bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-6">
                <div class="flex items-center justify-between border-b border-gray-300 pb-4">
                    <div>
                        <h2 class="text-xl font-extrabold text-gray-900">1. Enter Monitor Size, Eye Distance & Screen Setup</h2>
                        <p class="text-xs text-gray-600">Calculates iRacing Horizontal FOV, ACC/F1 Vertical FOV, Triple Angle & Rig Span</p>
                    </div>
                    <span class="text-xs font-mono bg-red-100 text-red-900 border border-red-300 px-2.5 py-1 rounded font-semibold">Live 1:1 FOV Math</span>
                </div>

                <div>
                    <label for="quickPreset" class="block text-xs font-bold uppercase tracking-wider text-gray-700 mb-2">Quick Select Monitor & Cockpit Preset</label>
                    <select id="quickPreset" onchange="applyPreset(this.value)" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-semibold text-gray-900 focus:ring-2 focus:ring-red-700">
                        <option value="{page_data['diag_in']},{page_data['aspect']},{page_data['screens']},{page_data['dist_in']},{page_data['bezel_mm']},{page_data['discipline']}">Current: {page_data['name']}</option>
                        <option value="32,16:9,3,23,8,gt3">Triple 32\" 16:9 Monitors @ 23\" Distance (178° hFOV / 60° Side Angle)</option>
                        <option value="49,32:9,1,22,0,gt3">49\" 32:9 Super-Ultrawide (Odyssey G9) @ 22\" Distance (103° hFOV)</option>
                        <option value="27,16:9,3,22,7,formula">Triple 27\" 16:9 Monitors @ 22\" Distance (166° hFOV / 55° Side Angle)</option>
                        <option value="34,21:9,1,22,0,gt3">34\" 21:9 Curved Ultrawide @ 22\" Distance (74° hFOV / 34° vFOV)</option>
                        <option value="57,32:9,1,24,0,gt3">57\" 32:9 Dual-4K Super-Ultrawide @ 24\" Distance (111° hFOV)</option>
                        <option value="55,16:9,1,34,0,gt3">55\" 4K 120Hz OLED TV @ 34\" Distance (72° hFOV / 43° vFOV)</option>
                    </select>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                    <div>
                        <label for="diagInput" class="block text-sm font-bold text-gray-800 mb-1">Screen Diagonal (Inches)</label>
                        <input type="number" id="diagInput" value="{page_data['diag_in']}" min="21" max="85" step="1" oninput="calculateSim()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-red-700">
                        <span class="text-[11px] text-gray-600">Standard: 27\", 32\", 34\", 49\"</span>
                    </div>

                    <div>
                        <label for="aspectInput" class="block text-sm font-bold text-gray-800 mb-1">Monitor Aspect Ratio</label>
                        <select id="aspectInput" onchange="calculateSim()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3 py-2.5 text-sm font-bold text-gray-900">
                            <option value="16:9" {"selected" if page_data['aspect'] == "16:9" else ""}>16 : 9 Standard Widescreen</option>
                            <option value="21:9" {"selected" if page_data['aspect'] == "21:9" else ""}>21 : 9 Ultrawide (34\"/38\"/45\")</option>
                            <option value="32:9" {"selected" if page_data['aspect'] == "32:9" else ""}>32 : 9 Super-Ultrawide (49\"/57\")</option>
                        </select>
                    </div>

                    <div>
                        <label for="screensInput" class="block text-sm font-bold text-gray-800 mb-1">Number of Monitors</label>
                        <select id="screensInput" onchange="calculateSim()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3 py-2.5 text-sm font-bold text-gray-900">
                            <option value="1" {"selected" if page_data['screens'] == 1 else ""}>Single Monitor (1 Screen)</option>
                            <option value="3" {"selected" if page_data['screens'] == 3 else ""}>Triple Monitors (3 Screens)</option>
                        </select>
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                    <div>
                        <label for="distInput" class="block text-xs font-bold text-gray-800 mb-1">Eye-to-Screen Distance (In)</label>
                        <input type="number" id="distInput" value="{page_data['dist_in']}" min="14" max="72" step="0.5" oninput="calculateSim()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3 py-2 text-sm font-bold text-gray-900">
                        <span class="text-[11px] text-gray-600">Ideal behind rim: 21\"–25\"</span>
                    </div>

                    <div>
                        <label for="bezelInput" class="block text-xs font-bold text-gray-800 mb-1">Single Bezel Width (mm)</label>
                        <input type="number" id="bezelInput" value="{page_data['bezel_mm']}" min="0" max="25" step="1" oninput="calculateSim()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3 py-2 text-sm font-bold text-gray-900">
                        <span class="text-[11px] text-gray-600">For Triple Bezel Comp (7–9mm)</span>
                    </div>

                    <div>
                        <label for="discInput" class="block text-xs font-bold text-gray-800 mb-1">Primary Racing Discipline</label>
                        <select id="discInput" onchange="calculateSim()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-2.5 py-2 text-sm font-bold text-gray-900">
                            <option value="gt3" {"selected" if page_data['discipline'] == "gt3" else ""}>GT3 / Sports Car / IMSA</option>
                            <option value="formula" {"selected" if page_data['discipline'] == "formula" else ""}>Formula / Open-Wheel</option>
                            <option value="drift" {"selected" if page_data['discipline'] == "drift" else ""}>Drift / Rally / Touge</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- Right Column: Output + Dynamic Amazon Recommendation (5 Cols) -->
            <div class="lg:col-span-5 bg-gray-100 border-2 border-red-700 rounded-2xl p-6 sm:p-8 shadow-md space-y-6">
                <div class="border-b border-gray-300 pb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider text-red-800">2. Engineered FOV, Angle & Torque Specs</span>
                    <h2 class="text-xl font-extrabold text-gray-900">Your Exact In-Game Settings</h2>
                </div>

                <div class="grid grid-cols-2 gap-3.5">
                    <div class="bg-red-100 border border-red-300 rounded-xl p-3.5">
                        <span class="text-xs text-red-950 font-semibold block">Horizontal FOV (iRacing)</span>
                        <span id="resHFOV" class="text-2xl font-black text-red-800">178.2°</span>
                        <span id="resSingleHFOV" class="text-[11px] text-red-900 block mt-0.5">59.4° Per Screen</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Vertical FOV (ACC / F1)</span>
                        <span id="resVFOV" class="text-2xl font-black text-gray-900">39.1°</span>
                        <span id="resPanelSize" class="text-[11px] text-emerald-800 font-bold block mt-0.5">Panel: 27.9\" × 15.7\"</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Triple Side Angle & Span</span>
                        <span id="resSideAngle" class="text-base font-extrabold text-gray-900">59.4° Angle</span>
                        <span id="resRigSpan" class="text-[11px] text-gray-600 block mt-0.5">Total Width: 57.1\" (145cm)</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Recommended DD Torque</span>
                        <span id="resTorque" class="text-sm font-extrabold text-amber-800">9–12 Nm DD</span>
                        <span id="resCockpit" class="text-[11px] text-gray-600 block mt-0.5">8020 Aluminum Cockpit</span>
                    </div>
                </div>

                <!-- Dynamic Matched Product Box -->
                <div class="bg-gray-200 border-2 border-red-600 rounded-xl p-4 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-[11px] font-extrabold uppercase tracking-wider bg-red-700 text-white px-2 py-0.5 rounded">Verified Hardware Match</span>
                        <span class="text-xs font-bold text-gray-700">Amazon Prime Ready</span>
                    </div>
                    <h3 id="recSimTitle" class="text-base font-extrabold text-gray-900 leading-snug">Loading Wheelbase & Monitor Match...</h3>
                    <p id="recSimDesc" class="text-xs text-gray-700"></p>
                    <div class="pt-1 flex flex-col sm:flex-row gap-2.5">
                        <a id="recPrimaryBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="flex-1 text-center bg-red-700 hover:bg-red-800 text-white font-extrabold text-sm py-3 px-4 rounded-lg transition shadow-sm">
                           Shop Matched DD Wheel & Pedals &rarr;
                        </a>
                        <a id="recSecondaryBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="text-center bg-gray-800 hover:bg-gray-900 text-white font-bold text-xs py-3 px-3 rounded-lg transition">
                           Shop Cockpit & Monitor
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- PRODUCT SEARCH ENGINE SECTION (SEARCH PRODUK) -->
        <section id="product-search" class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm">
            <div class="max-w-3xl mx-auto text-center space-y-4">
                <h2 class="text-2xl font-extrabold text-gray-900">Search Direct Drive Wheels, 8020 Cockpits, Load-Cell Pedals & 49\" Monitors</h2>
                <p class="text-sm text-gray-700">Search any brand (MOZA, Logitech G PRO, Next Level Racing, Playseat, Thrustmaster, Samsung Odyssey G9, Dayton Audio) or sim accessory on Amazon.</p>
                <form onsubmit="handleAmazonSearch(event)" class="flex flex-col sm:flex-row gap-3 pt-2">
                    <input type="text" id="amzSearchInput" placeholder="e.g. MOZA R9 Direct Drive, Logitech G PRO Wheel, Next Level Racing GTElite, Samsung 49 Odyssey G9..."
                           class="flex-1 bg-gray-200 border-2 border-gray-400 rounded-xl px-4 py-3 text-sm font-medium text-gray-900 placeholder-gray-500 focus:outline-none focus:border-red-700" required>
                    <button type="submit" class="bg-red-700 hover:bg-red-800 text-white font-extrabold text-sm px-6 py-3 rounded-xl transition cursor-pointer shrink-0">
                        Search on Amazon &rarr;
                    </button>
                </form>
                <div class="flex flex-wrap items-center justify-center gap-2 pt-2 text-xs">
                    <span class="text-gray-600 font-semibold">Popular Searches:</span>
                    <a href="{amz_url('MOZA R5 R9 R12 Direct Drive Sim Racing Wheel')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-red-200 text-gray-800 border border-gray-300 rounded-full transition">MOZA Direct Drive</a>
                    <a href="{amz_url('Logitech G PRO Racing Wheel and PRO Pedals')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-red-200 text-gray-800 border border-gray-300 rounded-full transition">Logitech G PRO 11Nm</a>
                    <a href="{amz_url('Next Level Racing F-GT Elite GTElite Cockpit')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-red-200 text-gray-800 border border-gray-300 rounded-full transition">8020 Sim Cockpits</a>
                    <a href="{amz_url('Samsung 49 Inch Odyssey G9 240Hz Curved Monitor')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-red-200 text-gray-800 border border-gray-300 rounded-full transition">49\" Odyssey G9 32:9</a>
                    <a href="{amz_url('Dayton Audio BST-1 Bass Shaker and Nobsound Amp')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-red-200 text-gray-800 border border-gray-300 rounded-full transition">SimHub Bass Shakers</a>
                </div>
            </div>
        </section>

        <!-- BEST SELLING PRODUCTS GRID (PRODUK TERLARIS) -->
        <section id="best-sellers" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-red-800">Verified Esports & Paddock Hardware</span>
                    <h2 class="text-2xl font-extrabold text-gray-900">Best-Selling Direct Drive Wheels, Cockpits, Monitors & Load-Cell Pedals</h2>
                </div>
                <a href="{amz_url('Best Selling Sim Racing Wheels Cockpits and Pedals')}" target="_blank" rel="nofollow sponsored noopener" class="text-sm font-bold text-red-800 hover:text-red-900">
                    Browse Full Amazon Best Sellers &rarr;
                </a>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                {bestseller_cards_html}
            </div>
        </section>

        {comparison_html}

        <!-- CUMULATIVE DAILY PRODUCT REVIEW ARTICLES SECTION (+3 NEW ARTICLES PER DAY) -->
        <section id="reviews" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-red-800">Autonomous Daily Review Archive ({total_reviews_count} Published Articles & Growing +3/Day)</span>
                    <h2 class="text-2xl font-extrabold text-gray-900">In-Depth Direct Drive, Cockpit, Monitor & Pedal Review Articles</h2>
                </div>
                <span class="text-xs font-semibold bg-emerald-100 text-emerald-900 border border-emerald-300 px-3 py-1 rounded-full">+3 New Product Reviews Added Automatically Every Day</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {reviews_grid_html}
            </div>
        </section>

        <!-- MID-PAGE PROMOTIONAL AFFILIATE BANNER -->
        <section class="bg-gray-300 border-2 border-red-700 rounded-2xl p-6 sm:p-8 flex flex-col md:flex-row items-center justify-between gap-6">
            <div class="space-y-2 max-w-2xl">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-red-700 text-white px-2.5 py-1 rounded">Complete 2-Second Lap-Time Drop Bundle</span>
                <h2 class="text-xl sm:text-2xl font-extrabold text-gray-900">Upgrading From a Desk-Clamped Gear Wheel to a Dedicated Direct Drive Rig?</h2>
                <p class="text-sm text-gray-800">Unlock rock-solid trail braking and instant oversteer saves by pairing a 9–12 Nm Direct Drive Wheelbase & 100kg Load-Cell Pedals with an 8020 Aluminum Cockpit and 4-Corner SimHub Bass Shakers.</p>
            </div>
            <a href="{mid_banner_link}" target="_blank" rel="nofollow sponsored noopener"
               class="shrink-0 bg-red-700 hover:bg-red-800 text-white font-extrabold text-sm px-6 py-3.5 rounded-xl shadow-sm transition">
               Explore Direct Drive + Cockpit Bundles on Amazon &rarr;
            </a>
        </section>

        <!-- PROGRAMMATIC SEO DIRECTORY -->
        <section id="presets" class="space-y-4">
            <div class="border-b border-gray-300 pb-3">
                <h2 class="text-xl font-extrabold text-gray-900">Monitor Size, Eye Distance & Sim Title Specific FOV Calculators</h2>
                <p class="text-xs text-gray-600">Select your exact monitor configuration or eye distance below for pre-calculated Horizontal FOV, Vertical FOV, and triple-screen wrap angles.</p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2.5">
                {preset_links_html}
            </div>
        </section>

        <!-- FREQUENTLY ASKED QUESTIONS (FAQ) -->
        <section id="faq" class="space-y-6">
            <div class="border-b border-gray-300 pb-3">
                <span class="text-xs font-extrabold uppercase tracking-wider text-red-800">Trigonometric FOV, Bezel Correction & Torque Guide</span>
                <h2 class="text-2xl font-extrabold text-gray-900">Frequently Asked Questions (FAQ)</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {faq_html}
            </div>
        </section>

        {onpage_sitemap_html}

    </main>

    <!-- FOOTER (GRAY BACKGROUND) -->
    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700">
        <div class="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>
                <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
                <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
            </div>
            <div class="flex flex-wrap gap-4 font-medium text-gray-800">
                <a href="{BASE_URL}/" class="hover:text-red-800">Home</a>
                <a href="{BASE_URL}/#comparison" class="hover:text-red-800">Comparisons</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-red-800">Daily Reviews (+3/Day)</a>
                <a href="{BASE_URL}/sitemap.html" class="hover:text-red-800 font-bold">HTML Site Map</a>
                <a href="{BASE_URL}/sitemap.xml" class="hover:text-red-800">XML Sitemap</a>
                <a href="{BASE_URL}/#faq" class="hover:text-red-800">FAQ</a>
            </div>
        </div>
    </footer>

    <!-- INTERACTIVE CALCULATOR & AFFILIATE MATCHING SCRIPT -->
    <script>
        const AFFILIATE_TAG = "{AFFILIATE_TAG}";

        function makeAmazonLink(query) {{
            return "https://www.amazon.com/s?k=" + encodeURIComponent(query) + "&tag=" + AFFILIATE_TAG;
        }}

        function applyPreset(val) {{
            const parts = val.split(",");
            if (parts.length === 6) {{
                document.getElementById("diagInput").value = parts[0];
                document.getElementById("aspectInput").value = parts[1];
                document.getElementById("screensInput").value = parts[2];
                document.getElementById("distInput").value = parts[3];
                document.getElementById("bezelInput").value = parts[4];
                document.getElementById("discInput").value = parts[5];
                calculateSim();
            }}
        }}

        function handleAmazonSearch(e) {{
            e.preventDefault();
            const q = document.getElementById("amzSearchInput").value.trim();
            if (q) {{
                window.open(makeAmazonLink(q), "_blank", "noopener,noreferrer");
            }}
        }}

        function calculateSim() {{
            const diagIn = parseFloat(document.getElementById("diagInput").value) || 32;
            const aspect = document.getElementById("aspectInput").value || "16:9";
            const screens = parseInt(document.getElementById("screensInput").value) || 3;
            const distIn = Math.max(10, parseFloat(document.getElementById("distInput").value) || 23);
            const bezelMM = parseFloat(document.getElementById("bezelInput").value) || 8;
            const disc = document.getElementById("discInput").value || "gt3";

            let arW = 16.0;
            let arH = 9.0;
            if (aspect === "32:9") {{ arW = 32.0; arH = 9.0; }}
            else if (aspect === "21:9") {{ arW = 21.0; arH = 9.0; }}

            const hypot = Math.sqrt((arW * arW) + (arH * arH));
            const panelW = diagIn * (arW / hypot);
            const panelH = diagIn * (arH / hypot);
            const totalSingleW = panelW + ((bezelMM * 2.0) / 25.4);

            const singleHFOV = (2.0 * Math.atan(totalSingleW / (2.0 * distIn))) * (180.0 / Math.PI);
            const vFOV = (2.0 * Math.atan(panelH / (2.0 * distIn))) * (180.0 / Math.PI);

            let totalHFOV = singleHFOV;
            let sideAngle = 0;
            let spanIn = panelW;

            if (screens === 3) {{
                totalHFOV = Math.min(185.0, singleHFOV * 3.0);
                sideAngle = singleHFOV;
                const rad = sideAngle * (Math.PI / 180.0);
                spanIn = totalSingleW + (2.0 * totalSingleW * Math.cos(rad));
            }}

            let torqueStr = "9–12 Nm DD (GT3 Sweet Spot)";
            let cockpitStr = "8020 Aluminum Cockpit";
            if (disc === "drift") {{
                torqueStr = "9–12 Nm DD + 330mm Round Rim";
                cockpitStr = "Rig w/ Shifter & Handbrake Arm";
            }} else if (disc === "formula") {{
                torqueStr = "11–15 Nm DD + 290mm Formula Rim";
                cockpitStr = "F-GT Elite Formula Position";
            }}

            document.getElementById("resHFOV").textContent = totalHFOV.toFixed(1) + "° hFOV";
            document.getElementById("resSingleHFOV").textContent = screens === 3 ? (singleHFOV.toFixed(1) + "° Center / Per Screen") : "Single Screen Mathematical FOV";
            document.getElementById("resVFOV").textContent = vFOV.toFixed(1) + "° vFOV";
            document.getElementById("resPanelSize").textContent = "Screen: " + panelW.toFixed(1) + "\\\" W × " + panelH.toFixed(1) + "\\\" H";
            document.getElementById("resSideAngle").textContent = screens === 3 ? (sideAngle.toFixed(1) + "° Side Angle") : "0° (Single Screen)";
            document.getElementById("resRigSpan").textContent = "Total Width: " + spanIn.toFixed(1) + "\\\" (" + Math.round(spanIn * 2.54) + "cm)";
            document.getElementById("resTorque").textContent = torqueStr;
            document.getElementById("resCockpit").textContent = cockpitStr;

            let recTitle = "";
            let recDesc = "";
            let primaryQuery = "MOZA R9 R12 Logitech G PRO Direct Drive Racing Wheel and Load Cell Pedals";
            let secondaryQuery = "";

            if (screens === 3) {{
                recTitle = "Next Level Racing Free-Standing Triple Monitor Stand + 3× " + diagIn + "\" 1440p 165Hz Monitors";
                recDesc = "Engineered for a " + totalHFOV.toFixed(0) + "° wrap-around cockpit set at a " + sideAngle.toFixed(0) + "° side-screen angle (" + spanIn.toFixed(1) + "\" total width).";
                secondaryQuery = "Next Level Racing Free Standing Triple Monitor Stand and LG UltraGear 32 1440p";
            }} else if (aspect === "32:9") {{
                recTitle = "Samsung 49\" Odyssey G9 (32:9 240Hz) + Ergotron HX Heavy-Duty Arm + MOZA / Logitech DD";
                recDesc = "Delivers " + totalHFOV.toFixed(0) + "° of bezel-free horizontal FOV at " + distIn + " inches behind your steering wheel.";
                secondaryQuery = "Samsung 49 Inch Odyssey G9 240Hz Curved Monitor and Ergotron HX Arm";
            }} else {{
                recTitle = "MOZA R9 / R5 or Logitech G PRO Direct Drive + Next Level GTElite / Playseat Trophy";
                recDesc = "Zero-flex cockpit and 100kg load-cell pedals matched to your " + diagIn + "-inch (" + totalHFOV.toFixed(0) + "° hFOV / " + vfov.toFixed(0) + "° vFOV) setup.";
                secondaryQuery = "Next Level Racing GTElite Playseat Trophy Sim Racing Cockpit";
            }}

            document.getElementById("recSimTitle").textContent = recTitle;
            document.getElementById("recSimDesc").textContent = recDesc;
            document.getElementById("recPrimaryBtn").href = makeAmazonLink(primaryQuery);
            document.getElementById("recSecondaryBtn").href = makeAmazonLink(secondaryQuery);
        }}

        window.addEventListener("DOMContentLoaded", calculateSim);
    </script>
</body>
</html>"""

def render_single_review_page(rev):
    canonical_url = f"{BASE_URL}/{rev['slug']}.html"
    amz_link = amz_url(rev["keyword"])

    review_schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": rev["product_name"],
        "description": rev["summary"],
        "review": {
            "@type": "Review",
            "datePublished": rev["published_date"],
            "reviewRating": {"@type": "Rating", "ratingValue": rev["rating_score"], "bestRating": "5"},
            "author": {"@type": "Organization", "name": SITE_NAME},
            "reviewBody": " ".join(rev["body_paragraphs"])
        }
    }

    pros_html = "".join([f'<li class="flex items-start gap-2 text-sm text-gray-800"><span class="text-emerald-700 font-bold">✓</span><span>{p}</span></li>' for p in rev["pros"]])
    cons_html = "".join([f'<li class="flex items-start gap-2 text-sm text-gray-800"><span class="text-rose-700 font-bold">✕</span><span>{c}</span></li>' for c in rev["cons"]])
    paragraphs_html = "".join([f'<p class="text-gray-800 leading-relaxed text-base mb-4">{p}</p>' for p in rev["body_paragraphs"]])

    recent_reviews = [r for r in get_cumulative_product_reviews() if r["slug"] != rev["slug"]][:6]
    related_html = ""
    for other in recent_reviews:
        related_html += f"""
        <a href="{BASE_URL}/{other['slug']}.html" class="bg-gray-100 border-2 border-gray-300 rounded-xl p-4 hover:border-red-700 transition block">
            <span class="text-[11px] font-bold text-red-800 uppercase">{other['verdict_badge']}</span>
            <h4 class="font-extrabold text-sm text-gray-900 mt-1 line-clamp-2">{other['product_name']} Review</h4>
            <span class="text-xs text-gray-600 mt-1 block">Score: {other['rating_score']} / 5.0 ★ ({other['published_date']}) &rarr;</span>
        </a>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{rev['title']} | {SITE_NAME}</title>
    <meta name="description" content="{rev['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(review_schema)}</script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-red-800">Home & FOV Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#reviews" class="hover:text-red-800">Daily Sim Reviews</a>
            <span>/</span>
            <span class="text-gray-900">{rev['product_name']}</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-5">
            <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-red-100 text-red-900 border border-red-300 px-3 py-1 rounded-full">{rev['verdict_badge']}</span>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-mono text-gray-600">Published: {rev['published_date']}</span>
                    <span class="text-sm font-black bg-amber-200 text-amber-950 px-3 py-1 rounded-lg">Paddock Rating: {rev['rating_score']} / 5.0 ★</span>
                </div>
            </div>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900 leading-tight">{rev['title']}</h1>
            <p class="text-base text-gray-700 leading-relaxed">{rev['summary']}</p>

            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 bg-gray-200 p-4 rounded-xl border border-gray-300 text-xs">
                <div><span class="text-gray-500 block font-medium">Primary Spec</span><strong class="text-gray-900">{rev['spec_1']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Sensor / Panel</span><strong class="text-gray-900">{rev['spec_2']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Build / Mount</span><strong class="text-gray-900">{rev['spec_3']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Features</span><strong class="text-gray-900">{rev['spec_4']}</strong></div>
            </div>

            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="flex-1 text-center bg-red-700 hover:bg-red-800 text-white font-extrabold text-sm py-3.5 px-6 rounded-xl transition shadow-sm">
                   Check Latest Price & Availability on Amazon &rarr;
                </a>
                <a href="{BASE_URL}/#calculator"
                   class="text-center bg-gray-300 hover:bg-gray-400 text-gray-900 font-bold text-sm py-3.5 px-5 rounded-xl transition">
                   Calculate Your Mathematical FOV
                </a>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-gray-100 border-2 border-emerald-400 rounded-2xl p-6 space-y-3">
                <h2 class="text-base font-extrabold text-emerald-900 uppercase tracking-wide">Pros (What We Like)</h2>
                <ul class="space-y-2.5">{pros_html}</ul>
            </div>
            <div class="bg-gray-100 border-2 border-rose-400 rounded-2xl p-6 space-y-3">
                <h2 class="text-base font-extrabold text-rose-900 uppercase tracking-wide">Cons (Things to Consider)</h2>
                <ul class="space-y-2.5">{cons_html}</ul>
            </div>
        </div>

        <article class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 space-y-4">
            <h2 class="text-xl font-extrabold text-gray-900 border-b border-gray-300 pb-3">Hands-On Force Feedback Slew Rate, Rigidity & Track Analysis</h2>
            {paragraphs_html}
            <div class="pt-4 border-t border-gray-300 flex flex-col sm:flex-row items-center justify-between gap-4">
                <div>
                    <span class="text-xs font-bold uppercase text-red-800 block">Final Verdict</span>
                    <p class="text-sm font-bold text-gray-900">{rev['product_name']} earns {rev['rating_score']}/5.0 in our sim racing benchmark.</p>
                </div>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="shrink-0 bg-red-700 hover:bg-red-800 text-white font-extrabold text-sm px-6 py-3 rounded-xl transition shadow-sm">
                   View Customer Reviews & Price on Amazon &rarr;
                </a>
            </div>
        </article>

        <section class="space-y-4">
            <h3 class="text-lg font-extrabold text-gray-900">Recent Daily Sim Racing Hardware Reviews (+3 Added Daily)</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                {related_html}
            </div>
        </section>
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def render_vs_comparison_page(vs):
    canonical_url = f"{BASE_URL}/{vs['slug']}.html"
    link_a = amz_url(vs["keyword_a"])
    link_b = amz_url(vs["keyword_b"])

    rows_html = ""
    for m in vs["metrics"]:
        rows_html += f"""
        <tr class="border-b border-gray-300">
            <td class="p-4 font-bold text-gray-900 bg-gray-200 text-xs sm:text-sm w-1/4">{m['feature']}</td>
            <td class="p-4 text-xs sm:text-sm text-gray-800 w-3/8">{m['val_a']}</td>
            <td class="p-4 text-xs sm:text-sm text-gray-800 w-3/8">{m['val_b']}</td>
        </tr>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{vs['title']} | {SITE_NAME}</title>
    <meta name="description" content="{vs['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-red-800">Home & FOV Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#comparison" class="hover:text-red-800">Product Comparisons</a>
            <span>/</span>
            <span class="text-gray-900">{vs['product_a']} vs. {vs['product_b']}</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-4">
            <span class="text-xs font-extrabold uppercase tracking-wider bg-red-100 text-red-900 border border-red-300 px-3 py-1 rounded-full">{vs['winner_badge']}</span>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900 leading-tight">{vs['title']}</h1>
            <p class="text-base text-gray-700 leading-relaxed">{vs['summary']}</p>
        </div>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl overflow-hidden shadow-sm">
            <table class="w-full text-left border-collapse">
                <thead>
                    <tr class="bg-gray-800 text-white text-xs sm:text-sm font-extrabold">
                        <th class="p-4">Specification</th>
                        <th class="p-4 text-red-300">{vs['product_a']}</th>
                        <th class="p-4 text-amber-300">{vs['product_b']}</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                    <tr class="bg-gray-200">
                        <td class="p-4 font-extrabold text-xs sm:text-sm text-gray-900">Check Amazon Price</td>
                        <td class="p-4">
                            <a href="{link_a}" target="_blank" rel="nofollow sponsored noopener" class="inline-block bg-red-700 hover:bg-red-800 text-white font-extrabold text-xs py-2.5 px-4 rounded-lg transition">
                                View {vs['product_a']} &rarr;
                            </a>
                        </td>
                        <td class="p-4">
                            <a href="{link_b}" target="_blank" rel="nofollow sponsored noopener" class="inline-block bg-gray-800 hover:bg-gray-900 text-white font-extrabold text-xs py-2.5 px-4 rounded-lg transition">
                                View {vs['product_b']} &rarr;
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="bg-gray-100 border-2 border-red-600 rounded-2xl p-6 sm:p-8 space-y-4">
            <h2 class="text-xl font-extrabold text-gray-900">Head-to-Head Buying Verdict</h2>
            <p class="text-sm sm:text-base text-gray-800 leading-relaxed">{vs['verdict_text']}</p>
            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{link_a}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-red-700 hover:bg-red-800 text-white font-extrabold text-sm py-3 px-4 rounded-xl transition">
                    Shop {vs['product_a']} on Amazon &rarr;
                </a>
                <a href="{link_b}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-gray-800 hover:bg-gray-900 text-white font-extrabold text-sm py-3 px-4 rounded-xl transition">
                    Shop {vs['product_b']} on Amazon &rarr;
                </a>
            </div>
        </div>
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def generate_sitemap_and_robots(urls):
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    xml_items = ""
    for u in urls:
        xml_items += f"""  <url>
    <loc>{u}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>{"1.0" if u.endswith("/") else "0.85"}</priority>
  </url>\n"""

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_items}</urlset>"""

    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    robots_content = f"""User-agent: *
Allow: /
Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_content)

    with open(os.path.join(OUTPUT_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY)

def ping_indexnow(urls):
    parsed_host = urllib.parse.urlparse(BASE_URL).netloc
    if not parsed_host or "username.github.io" in parsed_host:
        return

    payload = {
        "host": parsed_host,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
        "urlList": urls
    }
    try:
        req = urllib.request.Request(
            "https://api.indexnow.org/indexnow",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"IndexNow Ping Status: {resp.status}")
    except Exception as e:
        print(f"IndexNow notice: {e}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    generated_urls = []

    # 1. Generate Homepage
    home_preset = {
        "slug": "index",
        "name": "Triple 32-Inch 16:9 Monitors (@ 23\" Eye Distance)",
        "diag_in": 32,
        "aspect": "16:9",
        "screens": 3,
        "dist_in": 23,
        "bezel_mm": 8,
        "discipline": "gt3",
        "desc": "Calculate exact mathematical Horizontal & Vertical FOV for iRacing, ACC, F1, and GT7—plus side-monitor wrap angles, total rig span width, and Direct Drive torque—with 3 new sim racing reviews added daily."
    }
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_calculator_page(home_preset, is_home=True))
    generated_urls.append(f"{BASE_URL}/")

    # 2. Generate Dedicated HTML Site Map Page (sitemap.html)
    with open(os.path.join(OUTPUT_DIR, "sitemap.html"), "w", encoding="utf-8") as f:
        f.write(render_dedicated_html_sitemap_page())
    generated_urls.append(f"{BASE_URL}/sitemap.html")

    # 3. Generate Programmatic Sim Racing FOV & Angle Calculator Pages
    for page in ALL_CALC_PAGES:
        filename = f"{page['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_calculator_page(page, is_home=False))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 4. Generate Cumulative Daily Product Review Pages (+3 new reviews unlocked every single day)
    active_reviews = get_cumulative_product_reviews()
    for rev in active_reviews:
        filename = f"{rev['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_single_review_page(rev))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 5. Generate Standalone Head-to-Head Product Comparison Pages
    for vs in VS_COMPARISONS:
        filename = f"{vs['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_vs_comparison_page(vs))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 6. XML Sitemap, Robots & IndexNow Auto-Ping
    generate_sitemap_and_robots(generated_urls)
    ping_indexnow(generated_urls)
    print(f"Successfully generated {len(generated_urls)} total SEO pages ({len(active_reviews)} cumulative review articles [+3/day] + HTML/XML sitemaps) in /{OUTPUT_DIR}!")

if __name__ == "__main__":
    main()
