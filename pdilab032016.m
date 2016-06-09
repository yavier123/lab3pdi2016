clear all;close all;
clc
%Primero hay que hacer el entrenamiento para obtener el rho 
%para hacer el entramiento hay que : 
warning off

im(:,:,:,1)=imread('lunar1.png');
im(:,:,:,2)=imread('lunar2.png');
im(:,:,:,3)=imread('lunar3.png');
im(:,:,:,4)=imread('lunar4.png');

red=im(:,:,1);%se paramos la foto en sus canales RGB
green=im(:,:,2);
blue=im(:,:,3);
%ocupramos roypoly para obtener una matriz pero solo con lo del lunar 
%hacemos otra vez roypoly para obtener una matriz pero esta vezde la piel
%Al terminar con las mascaras nos ponemos a obtner lo que queremos: 


%mask=roipoly(im);


%mask2=roipoly(im);
%imshow(mask);
pixelesA=double([0;0;0]);
pixelesB=double([0;0;0]);
count =0;
countdepiel=0;
matrizdezeros=zeros(480,640);
%el primer for es para recorrer las imagenes
for q=1:4
    %el segundo for es para que la imagen pase R-G_B
  mask=roipoly(im(:,:,:,q));  
for c=1:3
 %el tercer for es para recorrer la imagen 1-480   
for i=1:480
%y el cuartor for apra recorrer de 1-640    
    for j=1:640
        %para el material A que seria el lunar
%luego para tenemos que en nuestra mascara si 
%avanzamos que al momento de pillar 1 en roypoly hacer
        if mask(i,j)==1
%donde hacemos una sumatoria del valor del pixel 0-255
%cada vez que pilla un 1 en la mascara 
            count=count+1;
            pixelesA(c,1)=pixelesA(c,1)+double(im(i,j,c,q)); 
        else
%luego en caso contrario , osea que fueran 0
%simplemente hacemos lo mismo pero lo definimos 
%como material B
 %para el mateiral B que seria la piel  
    countdepiel=countdepiel+1;
    pixelesB(c,1)=pixelesB(c,1)+double(im(i,j,c,q));
% y para las 2 variables hacemos una  cuenta para 
%obtener el promedio de los pixeles que aparecen 
%y asi tenmos el entramineto del material A y B 
        end  
    end
end
end 
end 

A1=pixelesA(1,1)/count;
A2=pixelesA(2,1)/count;
A3=pixelesA(3,1)/count;
B1=pixelesB(1,1)/countdepiel;
B2=pixelesB(2,1)/countdepiel;
B3=pixelesB(3,1)/countdepiel;

Ro=[A1/B1 A1/B2 A1/B3 A2/B1 A2/B2 A2/B3 A3/B1 A3/B2 A3/B3];
%%

prueba(:,:,:)=imread('lunar1.png');


for c=1:3
    
for i=1:480
    
    for j=1:640
        if prueba(c,i,j)==
            
            
        else
            
    countdepiel=countdepiel+1;
             
        end  
    end
end
end 



















