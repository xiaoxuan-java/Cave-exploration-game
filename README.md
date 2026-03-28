中文：

Cave-exploration-game（洞穴探险游戏）
一、游戏概述
•	游戏名称：Cave-exploration-game（可暂译为《深渊矿影》或《地心诡途》）
•	游戏类型：第一人称/第三人称洞穴探险、生存、恐怖、动作冒险
•	游戏风格：像素风（Minecraft风格）
•	目标平台：PC（Windows/macOS/Linux）
•	版权归属：xiaoxuan_java（xiaoxuan-java）
•	素材声明：引用少量Minecraft风格贴图，仅为艺术风格参考，与Mojang AB无任何关联。
二、核心玩法
1.	资源收集
•	玩家在随机生成的地下洞穴系统中探索，采集矿石等基础资源。
•	特殊资源仅出现在深层区域或危险区域（如“血矿”、“灵魂尘”），需特定工具或抗性等条件获取。
2.	合成系统
•	玩家通过工作台（Crafting Table）将资源合成为工具、武器、防具。
•	合成配方随探索进度逐步解锁。
3.	生存机制
•	饥饿值、生命值。
•	饥饿值过低影响移动与攻击；
•	理智值下降会导致幻觉、怪物出现频率增加、屏幕扭曲等恐怖效果。
4.	战斗与BOSS战
•	洞穴中存在多种敌对生物，具有AI巡逻、伏击、群体围攻等行为。
•	每层洞穴深处设有“守层BOSS”，击败后可解锁新区域与合成配方。
•	BOSS设计融合恐怖元素，如：
•	“地心之母”：巨大肉块状生物，会召唤小怪，弱点在背部发光核心；
•	“无面矿工”：身穿破旧矿工装，手持镐子，可瞬移并模仿玩家声音制造心理恐惧。
5.	关卡结构
•	洞穴分为多层（如：表层矿道→废弃矿井→熔岩深渊→灵魂墓穴→地心王座），每层环境、资源、敌人不同。
•	地图程序化生成，但关键路径与BOSS房固定，确保剧情推进。
三、恐怖与暴力元素说明
•	恐怖元素：
•	黑暗环境、突然惊吓（Jump Scare）、低语音效、幻觉系统；
•	剧情揭示洞穴曾为古代文明祭祀地，玩家探索实为唤醒沉睡邪神。
•	暴力元素：
•	战斗含血迹、断肢、怪物死亡动画（可设置“血腥度”开关）；
•	BOSS战包含处决动画（如用镐刺入眼球、引爆火药桶炸碎躯体）。
玩家提示：本游戏包含恐怖与暴力内容，不适合儿童或心理敏感者。请玩家自行评估承受能力。
四、美术与音效
•	美术风格：
•	像素化3D建模，低多边形+像素贴图，类似Minecraft但更阴暗；
•	光照系统强调“手电筒/火把”依赖，黑暗区域怪物更易出现。
•	音效设计：
•	环境音：滴水声、远处低吼、金属摩擦声；
•	动态音乐：探索时低沉氛围音乐，遇敌时节奏加快，BOSS战使用交响恐怖配乐。
五、剧情梗概
“你是一名矿工，为寻找失踪的哥哥进入‘黑岩洞穴’。随着深入，你发现这里并非普通矿坑——古老的符文、扭曲的尸体、低语的石像……你逐渐意识到，你不是来挖矿的，你是被‘选中’的祭品。”
•	多结局系统：
•	结局1（牺牲）：击败最终BOSS后选择自我献祭，封印邪神；
•	结局2（堕落）：吸收邪神之力，成为新BOSS；
•	结局3（逃脱）：找到隐藏通道逃离，但理智归零，现实世界开始扭曲。
六、技术实现建议
•	实现程序化洞穴生成算法（Perlin Noise + Cellular Automata）；
•	加入存档系统、成就系统、难度选择（普通/噩梦/自虐模式）。
七、版权与声明
•	本游戏由 xiaoxuan_java（xiaoxuan-java） 独立开发与拥有全部权利；
•	使用的部分贴图风格参考自Minecraft，仅为艺术致敬，与Mojang AB、Microsoft无任何关联；
•	禁止未经授权的二次分发、商业化或修改源码。
八、未来扩展
•	多人合作模式（2-4人联机探险）；
•	模组支持（Mod API）；
•	自定义洞穴编辑器。
游戏标语建议：
“挖得越深，越难回头。”
“黑暗不是空的——它在看着你。”

English:

📄 Game Design Document: Cave-exploration-game
I. Game Overview
Game Title: Cave-exploration-game (Working Titles: Abyssal Mine Shadows or Core Dread)
Genre: First/Third-Person Cave Exploration, Survival, Horror, Action-Adventure
Art Style: Pixel Art (Minecraft-style aesthetic)
Target Platform: PC (Windows/macOS/Linux)
Copyright: xiaoxuan_java (xiaoxuan-java)
Asset Disclaimer: Uses a small amount of Minecraft-style textures for artistic reference only. Not affiliated with Mojang AB.
II. Core Gameplay
Resource Gathering
Players explore a procedurally generated underground cave system to mine basic resources like ores.
Special resources (e.g., "Blood Ore," "Soul Dust") appear only in deep or hazardous zones and require specific tools or resistances to harvest.
Crafting System
Players use a Crafting Table to turn resources into tools, weapons, and armor.
Recipes are progressively unlocked as exploration advances.
Survival Mechanics
Hunger & Health: Low hunger affects movement and attack speed.
Sanity Meter: Decreasing sanity triggers hallucinations, increases monster spawn rates, and causes screen distortion (horror effects).
Combat & Boss Battles
Hostile mobs with AI behaviors such as patrolling, ambushing, and swarming.
"Floor Bosses" guard the depths of each layer; defeating them unlocks new areas and recipes.
Boss Concepts:
Mother of the Core: A massive fleshy organism that spawns minions; weak point is a glowing core on its back.
The Faceless Miner: Wears tattered gear, wields a pickaxe, can teleport, and mimics player sounds to induce psychological fear.
Level Structure
Multi-layered caves (e.g., Surface Mines → Abandoned Shafts → Magma Abyss → Soul Crypt → Core Throne). Each layer features unique environments, resources, and enemies.
Maps are procedurally generated, but key paths and Boss Rooms are fixed to ensure narrative progression.
III. Horror & Violence Content
Horror Elements:
Dark environments, Jump Scares, low-frequency audio, and hallucination systems.
Narrative reveals the caves were ancient sacrificial sites; the player is unknowingly awakening a sleeping evil god.
Violence Elements:
Combat includes blood splatter, dismemberment, and monster death animations (includes a "Gore Level" toggle).
Boss fights feature execution animations (e.g., stabbing an eye with a pickaxe, blowing up a body with gunpowder barrels).
Player Advisory: This game contains horror and violent content. Not suitable for children or those with psychological sensitivities. Please assess your tolerance before playing.
IV. Art & Audio
Art Style:
Pixelated 3D modeling, low-poly + pixel textures. Similar to Minecraft but significantly darker.
Lighting system emphasizes reliance on flashlights/torches; monsters spawn more frequently in the dark.
Audio Design:
Ambience: Dripping water, distant growls, metal grinding sounds.
Dynamic Music: Low-key atmospheric tracks for exploration, fast-paced rhythm for combat, and symphonic horror scores for Boss battles.
V. Story Synopsis
"You are a miner entering the 'Blackrock Caverns' to find your missing brother. As you delve deeper, you realize this is no ordinary mine—ancient runes, twisted corpses, whispering statues... You gradually realize you aren't here to mine. You are the 'chosen' sacrifice."
Multiple Endings:
Ending 1 (Sacrifice): Defeat the final boss and choose self-sacrifice to seal the evil god.
Ending 2 (Corruption): Absorb the god's power and become the new Boss.
Ending 3 (Escape): Find a hidden passage to escape, but with zero sanity, reality begins to distort.
VI. Technical Implementation
Implement procedural cave generation algorithms (Perlin Noise + Cellular Automata).
Include Save System, Achievements, and Difficulty Selection (Normal / Nightmare / Masochist Mode).
VII. Copyright & Disclaimer
Developed and fully owned by xiaoxuan_java (xiaoxuan-java).
Texture styles reference Minecraft as an artistic tribute; no affiliation with Mojang AB or Microsoft.
Unauthorized redistribution, commercialization, or source code modification is prohibited.
VIII. Future Expansion
Multiplayer Co-op Mode (2-4 players).
Mod Support (Mod API).
Custom Cave Editor.
Suggested Taglines
"The deeper you dig, the harder it is to turn back."
"The darkness isn't empty—it's watching you."
