/*                              28 KEY MATRIX / LAYOUT MAPPING

  ╭ ───────────────┬────────────────╮ ╭ ────────────────┬────────────╮
  │  0   1   2   3   │  4   5   6   7    │ │ LT4 LT3 LT2 LT1 │ RT1 RT2 RT3 RT4 │
  │  8   9  10  11   │ 12  13  14  15    │ │ LM4 LM3 LM2 LM1 │ RM1 RM2 RM3 RM4 │
  │ 16  17  18  19   │ 20  21  22  23    │ │ LB4 LB3 LB2 LB1 │ RB1 RB2 RB3 RB4 │
  ╰ ───────╮ 24 25  │ 26  27 ╭────── ─╯ ╰ ──────╮ LH2 LH1 │ RH1 RH2 ╭──── ─╯  
           ╰────────┴────────╯                  ╰─────────┴─────────╯             */

#pragma once

// left-top row
#define LT1  3
#define LT2  2
#define LT3  1
#define LT4  0

// right-top row
#define RT1  4
#define RT2  5
#define RT3  6
#define RT4  7

// left-middle row
#define LM1 11
#define LM2 10
#define LM3 9
#define LM4 8

// right-middle row
#define RM1 12
#define RM2 13
#define RM3 14
#define RM4 15

// left-bottom row
#define LB1 19
#define LB2 18
#define LB3 17
#define LB4 16

// right-bottom row
#define RB1 20
#define RB2 21
#define RB3 22
#define RB4 23

#define LH1 25  // left thumb keys
#define LH2 24

#define RH1 26  // right thumb keys
#define RH2 27
