/*
 * main.cc
 * Copyright (C) 2016 kaoru <kaoru@localhost>
 *
 * Distributed under terms of the MIT license.
 */
 
#include <google/protobuf/message.h> // protobufのヘッダーファイルを追加
#include "user.pb.h"
using namespace std;
using namespace google::protobuf; // protobufの名前空間を追加
#include <iostream>
 
int main(int argc, char const* argv[])
{
 
        userdb::User u1;
 
        u1.set_id("abc");
        u1.set_pw("pass1");
 
        string serialized_str;
 
        u1.SerializeToString(&serialized_str);
 
        cout << serialized_str<< endl;
 
        return 0;
}