# Genetic Brushes 
Genetic brushes is an image painter that mimics the process of painting of an image into 
a canvas. 

# Implementation 
This artificial intelligence project is powered on genetic algorithms where each brush in the painting 
represents an individual of a population, this brushes mutate and improve with time, thus creating 
more realistic paintings overall. To improve the perfomance of the algorithm we provide additional 
information to the brushes such as the color of the original image are their position, and the importance 
of that position. The importance of a position of the image is calculated on a convoluted filter of 
vertical and horizontal edges. The genetic algorithm applies three kind of operators; mutation, selection,
and crossover. Mutation works by randomizin a specific feature of the current generation of brushes. 
After the mutation a crossover between different pairs of individuals. Finally we select the brushes 
based on their importance as explained before.  
![genetic](docs/drawing.png)
 

# Requirements 

    opencv-python~=4.2.0.34
    numpy~=1.18.5
    
