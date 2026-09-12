# my-1st-love — Agent Skills Directory (Global)

> ### 🚨 CRITICAL AGENT INSTRUCTION & PATH FAIL-SAFE
> Before executing any task, check this index to locate a relevant skill.
> **CRITICAL CONTEXT:** Every skill listed below is installed **globally**, NOT inside this project repository. They live in the user's home directory: `C:\Users\hp\.agents\skills\` (bash: `~/.agents/skills/`).
> **If your skill-loading tool fails or claims it cannot find a skill, DO NOT QUIT.**
> Bypass the tool, use your direct file-reading tools, and manually open the `SKILL.md` file at the Absolute Path listed below.
> This project repo (`my-1st-love`) currently has **no project-local skills**; `C:\Users\hp\.claude\skills\` is empty.

A curated library of globally installed skills — organized by category and purpose.

---

## Overview

| Location | Count | Purpose |
| :--- | :--- | :--- |
| `~/.agents/skills/` | 89 skills | Global library: game dev engines, gameplay systems, HTML artifact/presentation skills, meta-routing |
| `~/.claude/skills/` | 0 skills | Empty |
| This repo (project-local) | 0 skills | Nothing installed in `my-1st-love` yet |
| **Total** | **89 skills** | *(88 auto-loadable + 1 `scholar-notes` (学霸笔记) — renamed from `unnamed-skill`)* |

---

## Meta & Routing (2)

| # | Skill | Path (global) | Description |
| :--- | :--- | :--- | :--- |
| 1 | router | `C:\Users\hp\.agents\skills\router\SKILL.md` | Routes any game-dev request to the right specialized skill(s): detects engine (Godot, Unity, Unreal, Bevy, Phaser, PixiJS, three.js, LÖVE, pygame, Roblox) and task. Start here when unsure which skill applies. |
| 2 | find-skills | `C:\Users\hp\.agents\skills\find-skills\SKILL.md` | Discover and install agent skills when the user asks "how do I do X" or "is there a skill that can...". Search: `npx skills find <query>`. |

---

## HTML Artifacts & Presentation (14)

| # | Skill | Path (global) | Description |
| :--- | :--- | :--- | :--- |
| 3 | html | `C:\Users\hp\.agents\skills\html\SKILL.md` | Self-contained single-file HTML artifacts — reports, explainers, landing pages, decks, tools. Implicit router; delegates wireframe/prototype/plan/diagram to specialists. |
| 4 | html-wireframe | `C:\Users\hp\.agents\skills\html-wireframe\SKILL.md` | Low-fidelity HTML wireframes — info hierarchy, navigation, task flow, responsive structure. |
| 5 | html-prototype | `C:\Users\hp\.agents\skills\html-prototype\SKILL.md` | Polished responsive HTML mockups and interactive prototypes (mockup = static, prototype = working flow). |
| 6 | html-plan | `C:\Users\hp\.agents\skills\html-plan\SKILL.md` | HTML plans/roadmaps — phases, owners, dependencies, acceptance checks. |
| 7 | html-diagram | `C:\Users\hp\.agents\skills\html-diagram\SKILL.md` | HTML diagrams — topology, sequence, process, state, hierarchy, timeline, matrix. |
| 8 | design-artifact | `C:\Users\hp\.agents\skills\design-artifact\SKILL.md` | Creative direction for HTML artifacts — palette, type pairing, layout, theming; avoids generic AI look. |
| 9 | dynamic-archify | `C:\Users\hp\.agents\skills\dynamic-archify\SKILL.md` | Animated architecture/workflow/sequence/data-flow/lifecycle diagrams as standalone HTML with SVG, theme toggle, PNG/JPEG/WebP/SVG/GIF/WebM export. Accepts plain language or Mermaid. |
| 10 | flowchart | `C:\Users\hp\.agents\skills\flowchart\SKILL.md` | 教育/科普流程图、概念图、原理演示的动画 HTML 页面（CSS/SVG 节点连线、流动箭头、hover 高亮）。 |
| 11 | ppt-animation | `C:\Users\hp\.agents\skills\ppt-animation\SKILL.md` | PPT 风格翻页 HTML 演示动画（暗色炫酷/暖色报纸/简约白主题），适合视频科普、技术讲解。 |
| 12 | card-theater | `C:\Users\hp\.agents\skills\card-theater\SKILL.md` | 侧边栏叙事 + 3D 卡片轮播演示动画 HTML（滚动翻页、Coverflow 3D、Focus 展开、荧光笔高亮）。 |
| 13 | network-protocol-viz | `C:\Users\hp\.agents\skills\network-protocol-viz\SKILL.md` | 网络协议可视化动画 HTML（TCP/IP、以太网帧、IPv4、路由、DHCP、HTTPS）。 |
| 14 | phone-ui-demos | `C:\Users\hp\.agents\skills\phone-ui-demos\SKILL.md` | "手机系统 UI 风格"电影化演示动画：锁屏通知、聊天、设置页、控制中心、App 界面逐镜头呈现。 |
| 15 | video-shot-demos | `C:\Users\hp\.agents\skills\video-shot-demos\SKILL.md` | "每镜头一个 HTML"高完成度演示动画（分镜页、录屏用动画网页、同步音效、角色吐槽）。 |
| 16 | scholar-notes (学霸笔记) | `C:\Users\hp\.agents\skills\scholar-notes\SKILL.md` | 手写笔记本风格单文件 HTML 学习笔记（技术内容/漏洞分析/知识总结 → 精美网页笔记）。Folder was auto-named `unnamed-skill`; renamed 2026-09-12 to match its `scholar-notes` trigger. |

---

## Engine Skills — Godot 4.7 (15)

| # | Skill | Path (global) | Description |
| :--- | :--- | :--- | :--- |
| 17 | godot-gdscript | `C:\Users\hp\.agents\skills\godot-gdscript\SKILL.md` | Idiomatic GDScript — static typing, lifecycle, @export/@onready, signals, await. |
| 18 | godot-nodes-scenes | `C:\Users\hp\.agents\skills\godot-nodes-scenes\SKILL.md` | Scene tree structure, PackedScene instancing, autoload singletons. |
| 19 | godot-2d-movement | `C:\Users\hp\.agents\skills\godot-2d-movement\SKILL.md` | CharacterBody2D + move_and_slide(): platformer run/jump, top-down 8-direction, slopes. |
| 20 | godot-3d-essentials | `C:\Users\hp\.agents\skills\godot-3d-essentials\SKILL.md` | 3D scenes — Node3D transforms, Camera3D, lighting, WorldEnvironment, GridMap. |
| 21 | godot-animation | `C:\Users\hp\.agents\skills\godot-animation\SKILL.md` | AnimationPlayer clips, AnimationTree state machines/blend spaces, code-driven Tweens. |
| 22 | godot-audio | `C:\Users\hp\.agents\skills\godot-audio\SKILL.md` | AudioStreamPlayer, buses/volume/effects, music vs SFX routing, beat sync. |
| 23 | godot-csharp | `C:\Users\hp\.agents\skills\godot-csharp\SKILL.md` | C#/.NET in Godot — partial classes, [Export], [Signal] events, GDScript↔C#. |
| 24 | godot-export | `C:\Users\hp\.agents\skills\godot-export\SKILL.md` | Export templates, presets (Win/macOS/Linux/Web/Android), headless CI exports, HTML5 COOP/COEP. |
| 25 | godot-multiplayer | `C:\Users\hp\.agents\skills\godot-multiplayer\SKILL.md` | ENetMultiplayerPeer, @rpc annotations, authority, MultiplayerSpawner/Synchronizer. |
| 26 | godot-physics | `C:\Users\hp\.agents\skills\godot-physics\SKILL.md` | RigidBody/StaticBody/Area/CharacterBody, collision layers vs masks, raycasts. |
| 27 | godot-resources | `C:\Users\hp\.agents\skills\godot-resources\SKILL.md` | Data-driven design with custom Resource classes, .tres files, ResourceLoader. |
| 28 | godot-shaders | `C:\Users\hp\.agents\skills\godot-shaders\SKILL.md` | Godot Shading Language — canvas_item (2D) and spatial (3D) shaders, uniforms, TIME. |
| 29 | godot-signals-groups | `C:\Users\hp\.agents\skills\godot-signals-groups\SKILL.md` | Event-driven gameplay with signals and node groups, Callables, call_group. |
| 30 | godot-tilemap | `C:\Users\hp\.agents\skills\godot-tilemap\SKILL.md` | TileMapLayer + TileSet — collision/navigation/custom data, terrain autotiling. |
| 31 | godot-ui-control | `C:\Users\hp\.agents\skills\godot-ui-control\SKILL.md` | Control nodes, anchors, Container layout, Theme resources, focus navigation. |

## Engine Skills — Unity 6.3 LTS (8)

| # | Skill | Path (global) | Description |
| :--- | :--- | :--- | :--- |
| 32 | unity-csharp-scripting | `C:\Users\hp\.agents\skills\unity-csharp-scripting\SKILL.md` | MonoBehaviour lifecycle, GameObject/component access, coroutines, Inspector serialization. |
| 33 | unity-animation | `C:\Users\hp\.agents\skills\unity-animation\SKILL.md` | Animator Controllers — states, transitions, blend trees, humanoid IK. |
| 34 | unity-physics | `C:\Users\hp\.agents\skills\unity-physics\SKILL.md` | Rigidbody movement/forces, colliders, triggers, raycasts, joints. |
| 35 | unity-input-system | `C:\Users\hp\.agents\skills\unity-input-system\SKILL.md` | Input System package — Input Actions, action maps, PlayerInput, rebinding. |
| 36 | unity-navmesh | `C:\Users\hp\.agents\skills\unity-navmesh\SKILL.md` | NavMesh baking (NavMeshSurface), NavMeshAgent.SetDestination, dynamic obstacles. |
| 37 | unity-scriptableobjects | `C:\Users\hp\.agents\skills\unity-scriptableobjects\SKILL.md` | SO architecture — config assets, event channels, runtime sets, decoupling. |
| 38 | unity-tilemap-2d | `C:\Users\hp\.agents\skills\unity-tilemap-2d\SKILL.md` | Grid + Tilemap, Tile Palette, rule tiles, runtime SetTile painting. |
| 39 | unity-build-pipeline | `C:\Users\hp\.agents\skills\unity-build-pipeline\SKILL.md` | Build/ship players — build settings, IL2CPP vs Mono, stripping, CI builds. |

## Engine Skills — Unreal Engine 5 (6)

| # | Skill | Path (global) | Description |
| :--- | :--- | :--- | :--- |
| 40 | unreal-blueprints | `C:\Users\hp\.agents\skills\unreal-blueprints\SKILL.md` | Blueprint Classes, Event Graph, Construction Script, variables/functions, event dispatchers. |
| 41 | unreal-cpp-gameplay | `C:\Users\hp\.agents\skills\unreal-cpp-gameplay\SKILL.md` | UCLASS/UPROPERTY/UFUNCTION, GameMode/Pawn/Character/PlayerController, Build.cs. |
| 42 | unreal-enhanced-input | `C:\Users\hp\.agents\skills\unreal-enhanced-input\SKILL.md` | Input Actions, Input Mapping Contexts, modifiers/triggers, ETriggerEvent binding. |
| 43 | unreal-behavior-trees | `C:\Users\hp\.agents\skills\unreal-behavior-trees\SKILL.md` | NPC AI with BT + Blackboard — Selector/Sequence, tasks, decorators, services, AIController. |
| 44 | unreal-niagara | `C:\Users\hp\.agents\skills\unreal-niagara\SKILL.md` | Niagara VFX — emitters, modules, User parameters, spawning from BP/C++. |
| 45 | unreal-packaging | `C:\Users\hp\.agents\skills\unreal-packaging\SKILL.md` | Package Project flow, Dev vs Shipping configs, cooking, BuildCookRun. |

## Engine Skills — Other Engines (16)

| # | Skill | Path (global) | Description |
| :--- | :--- | :--- | :--- |
| 46 | bevy-ecs | `C:\Users\hp\.agents\skills\bevy-ecs\SKILL.md` | Bevy (Rust) ECS — App/plugins, Components/Resources, Query/Commands, Time. |
| 47 | phaser-core | `C:\Users\hp\.agents\skills\phaser-core\SKILL.md` | Phaser 4 setup — Game config, Scene lifecycle, loader, cameras, scene transitions. |
| 48 | phaser-arcade-physics | `C:\Users\hp\.agents\skills\phaser-arcade-physics\SKILL.md` | Arcade Physics — bodies, velocity/acceleration/gravity, colliders/overlaps/groups. |
| 49 | pixijs-rendering | `C:\Users\hp\.agents\skills\pixijs-rendering\SKILL.md` | PixiJS v8 — async Application, Assets loading, Container/Sprite graph, ticker, render groups. |
| 50 | threejs-scene-setup | `C:\Users\hp\.agents\skills\threejs-scene-setup\SKILL.md` | three.js Scene/Camera/WebGLRenderer, setAnimationLoop, resize, OrbitControls. |
| 51 | threejs-gltf-loading | `C:\Users\hp\.agents\skills\threejs-gltf-loading\SKILL.md` | glTF/GLB via GLTFLoader, AnimationMixer, DRACO/Meshopt, KTX2 textures. |
| 52 | threejs-materials-lighting | `C:\Users\hp\.agents\skills\threejs-materials-lighting\SKILL.md` | MeshStandardMaterial PBR, ambient/hemisphere/directional lights, shadow maps, envMap/IBL. |
| 53 | love2d-core | `C:\Users\hp\.agents\skills\love2d-core\SKILL.md` | LÖVE 11.x — love.load/update/draw loop, delta-time, input, screen states. |
| 54 | pygame-core | `C:\Users\hp\.agents\skills\pygame-core\SKILL.md` | pygame-ce — init/event/update/draw loop, Surface/Rect blitting, Sprite/Group collision. |
| 55 | roblox-luau | `C:\Users\hp\.agents\skills\roblox-luau\SKILL.md` | Luau scripting — services, Instances, events, server Scripts vs LocalScripts, remotes. |
| 56 | roblox-datastores | `C:\Users\hp\.agents\skills\roblox-datastores\SKILL.md` | DataStoreService persistence — GetAsync/SetAsync/UpdateAsync in pcall, leaderboards. |
| 57 | roblox-networking | `C:\Users\hp\.agents\skills\roblox-networking\SKILL.md` | RemoteEvent/RemoteFunction hardening — server authority, validation, rate limits, replication. |
| 58 | roblox-physics | `C:\Users\hp\.agents\skills\roblox-physics\SKILL.md` | Assemblies, constraints, collision groups, raycasts, network ownership, cleanup. |
| 59 | roblox-ui | `C:\Users\hp\.agents\skills\roblox-ui\SKILL.md` | ScreenGui/PlayerGui, UDim2 layouts, safe insets, ScrollingFrames, gamepad focus. |
| 60 | roblox-characters | `C:\Users\hp\.agents\skills\roblox-characters\SKILL.md` | CharacterAdded/Removing, Humanoid, Animator, R6/R15 rigs, respawn-safe systems. |
| 61 | roblox-studio-workflow | `C:\Users\hp\.agents\skills\roblox-studio-workflow\SKILL.md` | Safe Studio edits — Explorer, Rojo projects, Attributes, CollectionService tags, testing. |

---

## Cross-Engine Game Systems (28)

| # | Skill | Path (global) | Description |
| :--- | :--- | :--- | :--- |
| 62 | game-ai | `C:\Users\hp\.agents\skills\game-ai\SKILL.md` | NPC/enemy decisions — FSMs, behavior trees, steering/flocking, A* pathfinding. |
| 63 | ai-behavior-trees-utility-ai | `C:\Users\hp\.agents\skills\ai-behavior-trees-utility-ai\SKILL.md` | Production behavior-tree runtime (Blackboard, composites, decorators) + Utility AI response curves. |
| 64 | dialogue-systems | `C:\Users\hp\.agents\skills\dialogue-systems\SKILL.md` | Branching dialogue — node/choice graphs, conditions, Ink vs Yarn Spinner vs custom runners. |
| 65 | level-design | `C:\Users\hp\.agents\skills\level-design\SKILL.md` | Blockout-to-playable workflow, player metrics, pacing/gating, encounter design. |
| 66 | game-feel | `C:\Users\hp\.agents\skills\game-feel\SKILL.md` | Juice — screen shake, hit-stop, tweens, squash & stretch, knockback, layered feedback. |
| 67 | camera-systems | `C:\Users\hp\.agents\skills\camera-systems\SKILL.md` | 2D follow with deadzone/look-ahead, 3D orbit with collision, multi-target framing, shake. |
| 68 | input-systems | `C:\Users\hp\.agents\skills\input-systems\SKILL.md` | Action mapping, rebinding with conflict detection, gamepad/touch, deadzones, coyote time. |
| 69 | physics-tuning | `C:\Users\hp\.agents\skills\physics-tuning\SKILL.md` | Fixed vs variable timestep, interpolation, CCD, jitter fixes, collision layers. |
| 70 | audio-design | `C:\Users\hp\.agents\skills\audio-design\SKILL.md` | Bus/mixer architecture, dB gain, sidechain ducking, adaptive music layering, beat sync. |
| 71 | performance-optimization | `C:\Users\hp\.agents\skills\performance-optimization\SKILL.md` | Profiler-first method — frame budget, CPU/GPU bottleneck, pooling, draw-call batching. |
| 72 | save-systems | `C:\Users\hp\.agents\skills\save-systems\SKILL.md` | What to serialize, slots, atomic crash-safe writes, schema migration, autosave. |
| 73 | procedural-gen | `C:\Users\hp\.agents\skills\procedural-gen\SKILL.md` | Seeded RNG, Perlin/Simplex noise, dungeon generation (BSP, random walk), loot tables. |
| 74 | create-game-assets | `C:\Users\hp\.agents\skills\create-game-assets\SKILL.md` | Plan/generate/normalize cohesive visual assets — sprites, tilesets, UI art, textures. |
| 75 | game-ui-ux | `C:\Users\hp\.agents\skills\game-ui-ux\SKILL.md` | HUDs/menus that survive every screen — anchors, aspect scaling, focus nav, screen stack. |
| 76 | game-jam | `C:\Users\hp\.agents\skills\game-jam\SKILL.md` | Ship under a jam deadline — scope to the clock, schedule, cut features, submit on time. |
| 77 | prototype-fast | `C:\Users\hp\.agents\skills\prototype-fast\SKILL.md` | Playable prototype in ~1 hour to answer "is it fun?" — greybox, timebox, keep/kill criteria. |
| 78 | platformer | `C:\Users\hp\.agents\skills\platformer\SKILL.md` | 2D platformer — coyote time, jump buffering, variable jump height, tiled levels. |
| 79 | puzzle | `C:\Users\hp\.agents\skills\puzzle\SKILL.md` | Grid/board puzzles — match-3 cascades, sokoban, rule resolution, scoring, undo. |
| 80 | roguelike | `C:\Users\hp\.agents\skills\roguelike\SKILL.md` | Turn-based grid dungeons — procedural levels, permadeath, FOV, loot tables. |
| 81 | rpg | `C:\Users\hp\.agents\skills\rpg\SKILL.md` | RPG systems — stats/leveling, inventory/equipment, quests, save/load, combat. |
| 82 | card-game | `C:\Users\hp\.agents\skills\card-game\SKILL.md` | Deckbuilders/TCG — card data, deck/hand/discard, draw/shuffle, turns, effect resolution. |
| 83 | visual-novel | `C:\Users\hp\.agents\skills\visual-novel\SKILL.md` | VN — branching script, character/background display, textbox with choices, save/skip/auto. |
| 84 | fps-shooter | `C:\Users\hp\.agents\skills\fps-shooter\SKILL.md` | FPS — move+mouse-look, hitscan/projectiles, weapons, health, enemy AI. |
| 85 | tower-defense | `C:\Users\hp\.agents\skills\tower-defense\SKILL.md` | TD — lane pathing, wave spawning, auto-targeting towers, economy, lives. |
| 86 | survival-crafting | `C:\Users\hp\.agents\skills\survival-crafting\SKILL.md` | Survival — resource gathering, crafting/tech tree, needs (hunger/temp), base building. |
| 87 | shader-programming | `C:\Users\hp\.agents\skills\shader-programming\SKILL.md` | Cross-engine GLSL/HLSL — vertex→fragment pipeline, UV math, dissolve, outline, fresnel, vignette. |
| 88 | itch-publish | `C:\Users\hp\.agents\skills\itch-publish\SKILL.md` | itch.io publishing — project page, butler push channels, versioning. |
| 89 | steam-publish | `C:\Users\hp\.agents\skills\steam-publish\SKILL.md` | Steamworks — depots/packages, steamcmd uploads, beta branches, release checklists. |

---

## Quick Reference

```
C:\Users\hp\                          ← global install root (~ in bash)
└── .agents\
    └── skills\                       ← 89 skills
        ├── router\, find-skills\                     (meta — 2)
        ├── html\ + 4 html-* specialists,             (HTML artifacts &
        │   design-artifact\, dynamic-archify\,        presentation — 14)
        │   flowchart\, ppt-animation\, card-theater\,
        │   network-protocol-viz\, phone-ui-demos\,
        │   video-shot-demos\, scholar-notes\
        ├── godot-*\            (Godot 4.7 — 15)
        ├── unity-*\            (Unity 6.3 — 8)
        ├── unreal-*\           (Unreal 5 — 6)
        ├── bevy-ecs\, phaser-*\, pixijs-rendering\,   (other engines — 16)
        │   threejs-*\, love2d-core\, pygame-core\,
        │   roblox-*\
        └── game-ai\, game-feel\, level-design\, ...   (cross-engine
            game systems & publishing — 28)             systems — 28)

C:\Users\hp\.claude\skills\           ← empty
<this repo>\                          ← no project-local skills yet
```

**How to load:** invoke via the `skill` tool by name (e.g. `skill("godot-physics")`), or read the `SKILL.md` directly at the absolute path above if tooling fails. To install more: `npx skills find <query>` → `npx skills add <owner/repo> --skill <name> --yes`.

---

*Last updated: September 12, 2026 — indexed all 89 global skills from `C:\Users\hp\.agents\skills\` (0 project-local, `~/.claude/skills/` empty). Renamed `unnamed-skill` → `scholar-notes` (学霸笔记) to match its own frontmatter triggers.*
