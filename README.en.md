# codeFarm The-Farmer-Was-Replaced Code Guide

#### Introduction
Game code guide for *The-Farmer-Was-Replaced*

#### Software Architecture
Code architecture description
Copy the corresponding file content into the game
Alternatively, download the code repository to the corresponding game save folder

#### Installation Tutorial
Download the zip package or clone to local

#### Usage Instructions
    Copy the corresponding file content into the game
    Alternatively, download the code repository to the corresponding game save folder

##### 1、Single Drone Version:
    f0.py                   Absolute movement code for drones, other codes depend on this file
    grass_v1.py             Hay harvesting code
    bush_v1.py              Bush harvesting code
    carrot_v1.py            Carrot harvesting code
    tree_v1.py              Tree planting and harvesting code with spacing
    sunflower_v1.py         Sunflower harvesting code, direct harvesting, not optimized for maximum leaf count
    sunflower_v2_water.py   Sunflower harvesting code, direct harvesting with watering, not optimized for maximum leaf count
    pumkin_v1.py            Pumpkin harvesting code
    pumkin_v2_water.py      Pumpkin harvesting code, optimized with watering compared to pumkin_v1.py
    cactus_v1.py            Cactus harvesting code
    snake.py                Snake game code v0, no collision or other optimizations, fast production but lower yield
    snake_v1.py             Snake game code v1, can run full cycles, uses left-area prioritization and left-to-right apple consumption for quick start
    snake_v2.py             Snake game code v2, compared to v1, follows Hamiltonian cycle when snake length reaches 0.6 of the farm
    Weird_byFertilizer.py   Weird_Substance acquisition code using fertilizer, consumes fertilizer
    Weird_byWeird.py        Weird_Substance production using Weird_Substance, improper distribution causes conflicts during planting
    Weird_byWeird_v2.py     Weird_Substance production code v2, proper distribution without conflicts, please use this version
    gold_dfs.py             Single-drone maze algorithm based on DFS and backtracking

##### 2、Multi-Drone Version
    The following are multi-drone versions. Unless specified, they account for uneven distribution between farm side length and maximum drone count.
    In such cases, the farm size is adjusted to allow equal distribution. For example, when farm size is 22 (expansion level 8) with 8 drones,
    the side length and drone count aren't integer multiples, so the farm side length is set to 16 for distribution.
    grass_v2_multi.py       Multi-drone Hay harvesting code
    tree_v2_multi.py        Multi-drone Wood harvesting code
    carrot_v2_multi.py      Multi-drone Carrot harvesting code
    sunflower_v2_multi.py   Multi-drone Sunflower harvesting code
    pumkin_v2_multi.py      Multi-drone Pumpkin harvesting code
    pumkin_v3_multi.py      Optimized multi-drone Pumpkin harvesting code, records bad pumpkin positions and only traverses them.
                            With 32 drones, 32*32 farm, max pumpkin tech, and energy, yield ~22M/min. Can unlock Pumpkin Master achievement.
    catcus_v2_multi.py      Multi-drone Cactus harvesting code
    weird_byweird_v3_mul.py Multi-drone Weird_Substance code, achieves densest distribution

##### 3、Mixed Planting Scripts - Requires 32 Drones
    mix_plant.py            Mixed planting code, 32 drones, single drone diamond distribution. Planting types can be modified (refer to Tree, Grass, Carrot replacements).
                            With max tech, production rate ~160M/min Wood, 36M/min Hay, 33M/min Carrot. Used to unlock Hay Master, Wood Master, and Carrot Master/Big Carrot Farmer achievements.
    gold_by_weird.py        Multi-drone 5*5 maze acceleration using Weird_Substance. Source: Bilibili UP "显性单推隐性d", UID 398353982.
                            Max level yield ~3.5M/min, can unlock Maze Master achievement.
    gold_dfs_multi.py       Multi-drone 32*32 DFS maze code, yield ~1M/min
    gold_dfs_multi_circl.py Multi-drone 32*32 DFS reusable maze code. Adds randomness to resolve drone convergence in repeated use, may temporarily stall due to conflicts, lower yield.

##### 4、Other Codes
    change_hat.py           Unlocks Fashion Show achievement
    full_auto.py            Full Automation achievement code
    full_auto_test.py       Full Automation achievement test code. After downloading full_auto.py and full_auto_test.py, directly run full_auto_test.py and wait.

#### Contributing

1.  Fork this repository
2.  Create a new Feat_xxx branch
3.  Commit your code
4.  Create a Pull Request