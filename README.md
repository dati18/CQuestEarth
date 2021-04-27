<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://user-images.githubusercontent.com/17342474/116276162-88592f80-a784-11eb-9861-8939f3db18c7.png">
    <img src="https://user-images.githubusercontent.com/17342474/116276162-88592f80-a784-11eb-9861-8939f3db18c7.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">CQuest Earth</h3>
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

CQuest.earth is the earth observation (EO) platform based on Google Earth Engine and data from Google Earth Engine Data Catalog, created by Julian Kremers, CTO of CQuest. The code base was written in JavaScript.

Althought Google Earth Engine is a features-rich platform for scientific analysis and visualiztion of geospatial datasets, it has some drawbacks e.g every returned values will be automatically stored as an ee object, which require getInfo() function to be called and slow down performance.

Our approach to this problem is refactoring the code from JavaSript to Python by using geemap, a Python package for interactive mapping with Google Earth Engine and was built upon ipyleaflet and ipywidgets, which enables users to analyze and visualize Earth Engine datasets interactively within a Jupyter-based environment.

### Built With

major frameworks that I used to build the project:

* [geemap](https://geemap.org/)
* [Google Earth Engine](https://earthengine.google.com/)
* [ipywidgets](https://ipywidgets.readthedocs.io/en/stable/)
* [ipyleaflet](https://ipyleaflet.readthedocs.io/en/latest/)

Datasets:

* [MODIS and LandSat](https://developers.google.com/earth-engine/datasets/catalog) datasets from Earth Engine Data Catalog
* [SoilGrids](https://git.wur.nl/isric/soilgrids/soilgrids.notebooks/-/blob/master/markdown/access_on_gee.md) from World Soil Information


<!-- GETTING STARTED -->
## Getting Started

Before you can use the app on your local computer, please follow the instruction from Dr. Qiusheng Wu, the creator of geemap:
https://github.com/giswqs/geemap or https://www.youtube.com/playlist?list=PLAxJ4-o7ZoPccOFv1dCwvGI6TYnirRTg3

### Prerequisites

geemap is available on PyPI...
  ```sh
  pip install geemap
  ```
... and conda-forge also
  ```sh
  conda create -n gee python
  conda activate gee
  conda install mamba -c conda-forge
  mamba install geemap -c conda-forge
  ```
  
### Installation

1. Sign up for Google Earth Engine account via https://earthengine.google.com/
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Create a python3 file and run this
   ```sh
   import geemap
   m = geemap.Map()
   m
   ```
   Running this will redirect you to Google Earth Engine, remember to copy your key and paste it to the Python file 
4. Run the code


<!-- USAGE EXAMPLES -->
## Usage

1. Dataset selection:
![datasets](https://user-images.githubusercontent.com/17342474/116273147-cc970080-a781-11eb-9e0f-06f89b03566e.JPG)

2. Plotting (from markers or polygons)
![Plotting1](https://user-images.githubusercontent.com/17342474/116273156-cdc82d80-a781-11eb-8bee-d49f9036f25a.JPG)
![Plotting1](https://user-images.githubusercontent.com/17342474/116273159-ce60c400-a781-11eb-9a8e-38c4893d6fe1.JPG)
![Plotting1](https://user-images.githubusercontent.com/17342474/116273162-ce60c400-a781-11eb-9239-8a5d445fb0a1.JPG)

3. Organic Carbon
![soc](https://user-images.githubusercontent.com/17342474/116273164-cef95a80-a781-11eb-8ce8-eff5aa5680b0.JPG)

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

Dat Nguyen - ngtiendat1804@gmail.com

Julian Kremers - julian@cquest.ai


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
