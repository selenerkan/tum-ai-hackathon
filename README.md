# DeepRay by DS@LMU for MI4People x TUM.ai Makeathon 2022

<p float="left">
    <img src="assets/figma-shots/app-home.png" alt="app-shot" width="150"/>
    <img src="assets/figma-shots/app-scan.png" alt="app-shot" width="150"/>
    <img src="assets/figma-shots/app-processing.png" alt="app-shot" width="150"/>
    <img src="assets/figma-shots/app-results.png" alt="app-shot" width="155"/>
</p>

**Topic:** Healthcare Computer Vision for Developing World  
**Topic Owner**: MI4People - Paul Springer   
**Team:** Nikolas Gritsch, Selen Erkan, Faheem Zunjani, Seunghee Jeong, I. Tolga Ozturk  

<hr>

## About

Further information can be found in our [pitch desk]().

## Description of the Solution

### Data Engineering

As can be seen below, the provided dataset suffers terribly from imbalance between the classes. 



To tackle this, we implement several strategies described in the next subsections.

#### Balanced Data Sampling

- Over-sampled rare classes from the full dataset
- Under-sampled overrepresented classes

#### Smart Data Augmentation

The provided standard dataset in our opinion is not very representative of the data that our model
will face in the real world, especially in the developing countries.   
In order to tackle this, we apply several data augmentation strategies, especially to balance out the rare classes 
as shown below:

| Original                                                          | Horizontal Flip                                                     | Affine Rotation                                                    | 
|-------------------------------------------------------------------|---------------------------------------------------------------------|--------------------------------------------------------------------|
| <img src="assets/data-aug/original.jpeg" alt="xray" width="150"/> | <img src="assets/data-aug/horiz-flip.jpeg" alt="xray" width="150"/> | <img src="assets/data-aug/rot.jpeg" alt="xray" width="150"/> |

| Color Jitter                                                          | Contrasting                                                       | Random Perspective                                                          | 
|-----------------------------------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <img src="assets/data-aug/color-jitter.jpeg" alt="xray" width="150"/> | <img src="assets/data-aug/contrast.jpeg" alt="xray" width="150"/> | <img src="assets/data-aug/random-perspective.jpeg" alt="xray" width="150"/> |

| Gaussian Blur                                                          |  
|------------------------------------------------------------------------|
| <img src="assets/data-aug/gaussian-blur.jpeg" alt="xray" width="150"/> | 

We probabilistically applied a few/all of these augmentations to generate even more images.

#### Model Development

#### Model Distillation

#### Mobile App

#### 

### Instructions 


### Acknowledgement

We thank Paul Springer from MI4People for giving a detailed deep dive into the project and his feedback 
during the development of the product. 


