/** 
  * @mainpage Sorting.cpp
  * @authors Liz Boese
  * With Modifier Kevin D. Rau 
  * @date 11/17/2014
  * @section intro Introduction 
  * Homework for Doxygen to generate documentation
  * Sorting.pp C++ file for sorting intergers 
  *
  * @section body Homework Questions
  * 1. used Single Row Comments for the top for Name/Date
  * 2. used Mutli-Row Comments for large comments such as this
  * 3. Using QT style as well in this block of comments 
  * 4. Also used Single Line QT style for single comments 
  * 5. Also use JavaDoc Autobrief in top comments for HTTP output
  */

#include <iostream>
using namespace std;

/**
  * @param *i is a pointer to an integer value
  * @param *j is a pointer to an integer value
  */
void change(int *i, int *j)
{
int temp = *j; /*! and integer value of dereferenced pointer value */
 *j = *i;       /*! setting deref pointer j to deref pointer i */
*i = temp;      /*! temp pointer i value set to temp */
}


/**
  * @param *start - pass in pointer to first integer in array
  * @param *end - pass in pointer to last integer in array
  */
int *toplace(int *start, int *end)
{
    int *i = start, *j= end; //! set pointers *i, *j to variable start/end

    while(i<=j) //! use while loop to run through array and determine placement 
    {
    for(; *i<=*start && i<=end; i++);
    for(; *j>=*start && start+1<=j; j--);   
    if (i<j) change(i++,j--); 
    }

    change(start,i-1); 
    return i-1;
}

/**
  * @param *start takes in pointer start that is first integer in array
  * @param *end takes in a pointer end that is end integer in array
  */

void sort(int *start, int *end)
{
    if (start >= end) return; //! @return return @if start is > end 

    for(int *debug = start;debug<=end;debug++) std::cout<<*debug <<" ";
    std::cout<<std::endl;  //! std::cout<<std::endl; this and...

    int *temp = start;
    temp = toplace(start,end);

    for(int *debug = start;debug<=end;debug++) std::cout<<*debug <<" ";
    std::cout<<std::endl; //!...std::cout<<std::endl; this are only to "see under the hood"
    std::cout<<std::endl;

    sort(start,temp-1); //! passing in @param start and @param temp-1 in recursively
    sort(temp+1,end);   //! passing in @param temp -1 and @param end in recursively
}
/**
  * @main main
  * @param argc takes in first parameter
  * @param char* argv[] takes in seconds pointer paramter that points to an array of int
  * 
  */

int main(int argc, char* argv[]) 
{
    int A[] = {5,14,8,12,1,2,11,15,6,9,7,3,13,4,10}; //! build the array
    int n = sizeof (A) / sizeof(A[0]); 

    sort(A, &A[n-1]); //!pass in the array into sort and dereferenced integer values

    for (int i =0; i<n; i++) std::cout<<A[i] <<" "; //! @print 

    return 0; //!@return returns 0
}