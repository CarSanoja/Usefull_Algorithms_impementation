#define _USE_MATH_DEFINES

#include <iostream>
#include <math.h>

using namespace std;

double f(double mu, double sigma2, double x)
{
    //Use mu, sigma2 (sigma squared), and x to code the 1-dimensional Gaussian
    double prob = 1.0 / sqrt(2.0*M_PI*sigma2) * exp(- pow((x - mu), 2.0)/ (2.0*sigma2));
    return prob;
}