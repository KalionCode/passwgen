
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


  <h3 align="center">WordGen</h3>

  <p align="center">
    An flexible wordlist generation framework
    <br />
    <!-- <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
    <!-- <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a> -->
    ·
    <!-- <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a> -->
    ·
    <!-- <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a> -->
    ·
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
WordGen is a wordlist generation framework that is primarily targeted for passwords. It can be assisted with social engineering to generate any targets as WordGen uses a keyword-combination approach rather than hardcoded algorithms. For each keyword combination, you then can use built-in or user-defined 'formatter' functions to manipulate and generate more entries based on the original combination.


<!-- GETTING STARTED -->
## Getting Started

The project come with a default preset and can be used straight out of the box.

### Prerequisites

* Python 3.4+
* Standard library

### Installation

First, clone the repositry
   ```sh
   git clone hhttps://github.com/KalionCode/wordgen.git
   ```
Then install the locally cloned package with ```pip```
  ```sh
  cd wordgen 
  pip install -e .
  ```
or install directly from the ```pip``` repositry **(waiting for approval)**
  ```sh
  pip install wordgen
  ```



<!-- USAGE EXAMPLES -->
## Usage
WordGen uses a keyword combination approach on generating entries. What that means is that you basically give WordGen a list of keywords and it returns you different combinations of those keywords. The most basic usage would be:
```python
import wordgen
@wordgen.utils.registerU(2)
def someFunction(fstr, config , usedKeywords):
  print(fstr)

wordgen.generateWordList(['foo', 'bar'])

# output: 
# foofoofoo
# ...
# barbarfoo
# barbarbar
```
The ```import``` statement imports the packages related to WordGen. The decorator ```wordgen.utils.registerU()``` is used to register the block of code running in the specified loop (if in the n-th loop that means the loop will generate entries consisting n element)


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the GPLv3 License. See `LICENSE` for more information.



<!-- CONTACT -->
<!-- ## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name) -->



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
