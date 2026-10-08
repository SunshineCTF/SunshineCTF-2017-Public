Port Assignments
-----

Port assignment convention (`port = yycnn`):
- `yy` = last two digits of the competition year (17 for SunshineCTF 2017)
- `c`  = category: 0 pwn, 1 reversing, 2 scripting, 3 web, 4 crypto, 5 misc
        (also forensics/other), 6 speedrun, 7 pegasus
- `nn` = challenge index within the category (ordered by point value then name)

Raw TCP challenges: `nc ctf.hackucf.org <port>`.
HTTP(S) web challenges are served at `<slug>.ctf.hackucf.org` and bound to
`127.0.0.1:<port>` behind nginx (see the `nginx/` fragments).

| Challenge Name | Category | Author | Directory | Host | Port | Connection |
|----------------|----------|--------|-----------|------|-----:|------------|
| Prepared | Pwn | guyinatuxedo | Pwn/Prepared | ctf.hackucf.org | 17001 | `nc ctf.hackucf.org 17001` |
| The Memory Remains | Pwn | guyinatuxedo | Pwn/The-Memory-Remains | ctf.hackucf.org | 17002 | `nc ctf.hackucf.org 17002` |
| Notetorious | Pwn | C0deH4cker | Pwn/Notetorious | ctf.hackucf.org | 17003 | `nc ctf.hackucf.org 17003` |
| Alternative Solution | Reversing | guyinatuxedo | Reversing/Alternative-Solution | ctf.hackucf.org | 17101 | `nc ctf.hackucf.org 17101` |
| Wasteland | Reversing | guyinatuxedo | Reversing/Wasteland | ctf.hackucf.org | 17102 | `nc ctf.hackucf.org 17102` |
| Fallout Comrade | Scripting | vraelvrangr | Scripting/falloutcomrade | ctf.hackucf.org | 17201 | `nc ctf.hackucf.org 17201` |
| Low High | Scripting | vraelvrangr | Scripting/lowhigh | ctf.hackucf.org | 17202 | `nc ctf.hackucf.org 17202` |
| Maze Runner | Scripting | vraelvrangr | Scripting/mazerunner | ctf.hackucf.org | 17203 | `nc ctf.hackucf.org 17203` |
| Easy1 | Web | kablaa | Web/easy1 | easy1.ctf.hackucf.org | 17301 | https://easy1.ctf.hackucf.org |
| Easy2 | Web | kablaa | Web/easy2 | easy2.ctf.hackucf.org | 17302 | https://easy2.ctf.hackucf.org |
| Zombiedex | Web | kablaa | Web/zombiedex | zombiedex.ctf.hackucf.org | 17303 | https://zombiedex.ctf.hackucf.org |
| Vanity | Crypto | m0niker_ | Crypto/vanity | ctf.hackucf.org | 17401 | `nc ctf.hackucf.org 17401` |
| The Oracle | Crypto | vraelvrangr | Crypto/the_oracle | ctf.hackucf.org | 17402 | `nc ctf.hackucf.org 17402` |
