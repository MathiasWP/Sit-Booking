# ✨ Workout booking for lazy people

tldr; this project contains 2 different ways to book training on sits websites: 1 via their original website with Feide login (slow) and one on their ibooking website with a sit user (fast).

### Packages used
- selenium (`pip3 install selenium`)
- python-dotenv (`pip3 install python-dotenv`)

### Usage 

**Recommended (but not required)**: Create an .env file in the root of the project and declare your login-credentials there. If you don't do this, then you will have to replace the dotenv-configurations with your hardcoded credentials.

Expected values in .env file:
- Feide-login: "username", "password"
- Ibooking/sit-login: "telephone", "password"


**To book via SIT's original website via Feide (slow):**
```
python3 sit-feide.py
```

**To book via SIT's ibooking website via SIT (fast):**
```
python3 sit-ibooking.py
```
