#include <iostream>
#include <math.h>
#include <tuple>

using namespace std;

double new_mean, new_var;

// This function perform the measurment update.
// INPUT: mean and variance of prior belief and measurment
// OUTPUT: the new mean and variance in form of tuple
tuple<double, double> measurement_update(double mean1, double var1, double mean2, double var2)
{
    new_mean = (mean1*var2 + mean2*var1)/(var1 + var2);
    new_var =  1 / ( (1/var1) + (1/var2) );
    return make_tuple(new_mean, new_var);
}