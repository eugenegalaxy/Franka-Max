Franka Max is a part of a larger project "Max" that is made to communicate with robots 
through audio/visual information given by users. 
Franka Max will be based on a Franka Web API made by Jevgenijs Galaktionovs, https://github.com/eugenegalaxy/Franka-Galaxy


Task required from Franka robot:
Assist an operator by fetching him objects from the workspace

Objects:
Bottom cover
PCB
x2 Fuses
Top cover

Optional/next-step fetures: Colors of covers
White
Blue
Black

Franka skills needed:
Simple motions to a predifined various positions
Force based grasps with varying force (very low force for fuses)


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center"> Franka Max</h3>

  <p align="center">
    A beginning of a smart future with virtual assistants.
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Hey everyone, I am Jevgenijs `Galaxy` Galaktionovs. This project is a collection of some scripts that can be used to integrate with Franka Max general work done by Chen and Dimitris, MP Lab, AAU.

In case if this README file is not sufficient or more questions arise, feel free to contact me at **jevgenygalaktionov@gmail.com**.

<!-- GETTING STARTED -->
## Getting Started

Clone repository and run the scripts with `python3`.

### Prerequisites
- Python 3
- Franka Robot
- Account on Franka Desk Web interface
<!-- USAGE EXAMPLES -->
### File description

The repository consists of 4 python files:
- `FrankaWebAPI.py`: A class with methods to use Franka Desk functionality through a python script. Based on REST API calls. Must provide login and password in the your application script.
- `FrankaMax.py`: A class object to control Franka with REST API calls to Franka Desk web interface. Designed as module that can communicate with Max project and execute some actions on Franka robot. Check `assembly_task.py` to see how to use it together with `intent_generator.py` class.
- `intent_generator.py`: An example method of how commands could come from higher-level code, like MAX interface. An intent is a dictionary object that contains a command, a specification, and description. Check `assembly_task.py` to see how to use it together with `FrankaMax.py` class.

- `assembly_task.py`: A demo on how to use intent generation and FrankaMax class together to execute actions. This script calls 'execute' tasks that are locted in Franka Desk web interface. NOTE: it calls specific tasks with specific names that exist specifically on OUR Franka account.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- CONTACT -->
## Contact
Jevgenijs Galaktionovs - [Really A Robot](www.reallyarobot.com) - jga@reallyarobot.com

Chen Li  - postdoc at Department of Materials and Production, AAU - cl@mp.aau.dk
