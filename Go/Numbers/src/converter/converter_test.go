package converter

import "testing"

func TestGetPiWhenNegativeOrZero(t *testing.T) {
	value, err := FindPiToNthDigit(-1)
	if err != nil {
		t.Error(err.Error())
	}
}
