#include <boost/test/minimal.hpp>
#include "palindrome.h"

int test_main(int argc, char **argv)
{
    BOOST_CHECK(Text::is_palindrome("asd") == false);
    BOOST_CHECK(Text::is_palindrome("kajak") == true);
    BOOST_CHECK(Text::is_palindrome("") == false);
    BOOST_CHECK(Text::is_palindrome("palindrome") == false);
    BOOST_CHECK(Text::is_palindrome("mama") == false);
    BOOST_CHECK(Text::is_palindrome("Kajak") == true);

    return 0;
}