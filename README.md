# Dragonfly
Dragonfly is a 3D printed quad-copter capable of targeting with AI system and shooting foam balls. Development was started as part of an ASME competition. The competition was to develop a weapon to gain an advantage in NNU's on campus game, Humans vs Zombies. Which involves humans shooting zombies with nerf guns. Zombies must wear red headbands so they can be identified. Most other competitors designed Nerf gun mods to increase power or fire rate. Me and my partner decided we were going to build an autonomous drone that shoots nerf balls.

Note: This project is still in development.

Current Progress:
- [x] Processor
  - Raspberry Pi
- [x] Controls 
  - Currently using a PS4 Controller connected with bluetooth to laptop/phone. Transmitted through websockets using processing.
- [x] Detecting people 
  - An FRCNN has been trained to detect people, may switch to YOLO object detection
- [x] Firing Mechanism 
  - The mechanism has been 3D printed and works without being attached to the drone
  - Adjustments may (will) be necessary to fire in flight
- [ ] Body Design
  - A body was printed and tested to fly, but the arms were too weak and broke
  - A new body is being developed
- [ ] Stability
  - I am currently working on implementing a PID Controller
  - There may be an issue with the brushless motors we purchased being too low quality
  - They sometimes struggle with maintaining the speed they are set at (without any load)
- [ ] Targeting/Following
  - I have implemented a following system on a LEGO Mindstorm car that uses pixel detection
  - That system rotates the car to follow the center of area of the detected object
  - That system should be able to be transferred to the quadcopter with the exception of a different object detection method


This repository includes submodules so when cloning clone with:
git clone --recurse-submodules https://github.com/aborger/Dragonfly

Read more about submodules at:
https://git-scm.com/book/en/v2/Git-Tools-Submodules
