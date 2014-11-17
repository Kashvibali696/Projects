#ifndef PALINDROME_H
#define PALINDROME_H

#include <iostream>
#include <cmath>
#include <cctype>

class Text {
public:
    static bool is_palindrome(std::string);
};

bool Text::is_palindrome(std::string text) {
    int len = text.length();
    if (len == 0) {
        return false;
    }

    int mid = floor(len / 2);

    for (int i = 0; i <= mid; ++i)
    {  
        if (tolower(text[i]) != tolower(text[len - 1 - i]))
            return false;
    }

    return true;
}

#endif
