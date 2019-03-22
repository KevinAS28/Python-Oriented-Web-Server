#include <iostream>
#include <fstream>
#include "check_file.h"
#include <cstdio>
#ifndef REPORT_OWS
#define REPORT_OWS
std::string report(char name[])
{
 std::fstream file(name, std::ios::in|std::ios::binary);
 file.seekg(0, std::ios::end);
 int count = file.tellg();
 char hasil[count];
 file.seekg(0, std::ios::beg);
 file.read(hasil, count);
 file.close();
 return hasil;
}
template <class anything>
int interview(anything any, const char name[], int len)
{
 if (check_file(name))
 {
  try {std::remove(name);}catch (...) {}
 }
 std::fstream file(name, std::ios::out|std::ios::binary|std::ios::app);
 file.write(any, len);
 file.close();
}
#endif
//terusin kalo mau, buat python juga
//notasi juga (challenge)

