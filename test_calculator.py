import pytest
import unittest
from calculator import *

@pytest.fixture
def calc():
    return calculator()

class TestAdd:
    def test_add_two_positive_ints(self,calc):
        assert calculator.add(5,6) == 11

    def test_add_two_negative_ints(self,calc):
        assert calculator.add(-6,-7) == -13

    def test_add_one_postive_one_negative_int(self,calc):
        assert calculator.add(-6,8) == 2

    def test_add_zero_and_int(self,calc):
        assert calculator.add(0,2) == 2

    def test_add_zero_and_zero(self,calc):
        assert calculator.add(0,0) == 0

    def test_add_two_floats(self,calc):
        assert calculator.add(4.20,6.7) == pytest.approx(10.9)

    def test_add_boundary(self,calc):
        assert calculator.add(98490382498390484324424242343424342342424234324324645645646,2) == 98490382498390484324424242343424342342424234324324645645648

    def test_add_large_nums(self,calc):
        assert calculator.add(1111111111111,1111111111111) == 2222222222222

class TestSubtract:
    def test_subtract_two_postive_ints_positive_result(self,calc):
        assert calculator.subtract(6, 5) == 1

    def test_subtract_two_postive_ints_negative_result(self,calc):
        assert calculator.subtract(5,6) == -1

    def test_subtract_zero_from_num(self,calc):
        assert calculator.subtract(6,0) == 6

    def test_subtract_num_from_zero(self,calc):
        assert calculator.subtract(0,6) == -6

    def test_subtract_two_negative_ints(self,calc):
        assert calculator.subtract(-6,-4) == -2

    def test_subtract_positive_from_negative(self,calc):
        assert calculator.subtract(-6,4) == -10

    def test_subtract_negative_from_positive(self,calc):
        assert calculator.subtract(4,-6) == 10

    def test_subtract_two_floats(self,calc):
        assert calculator.subtract(6.9,4.2) == 2.7

    def test_subtract_zero_from_zero(self,calc):
        assert calculator.subtract(0,0) == 0

    def test_subtract_boundary(self,calc):
        assert calculator.subtract(2222222222222,1111111111111) == 1111111111111

class TestMultiply:
    def test_multiply_two_postive_ints(self,calc):
        assert calculator.multiply(5,6) == 30

    def test_multiply_two_negative_ints(self,calc):
        assert calculator.multiply(-6,-7) == 42

    def test_multiply_one_positive_one_negative_num(self,calc):
        assert calculator.multiply(-6,8) == -48

    def test_multiply_non_zero_by_zero(self,calc):
        assert calculator.multiply(0,2) == 0

    def test_multiply_zero_by_zero(self,calc):
        assert calculator.multiply(0,0) == 0

    def test_multiply_two_floats(self,calc):
        assert calculator.multiply(4.20,6.7) == pytest.approx(28.14)

    def test_multiplication_boundary_value(self,calc):
        assert calculator.multiply(123456789, 123456789) == 15241578750190521

    def test_multiply_int_and_float(self,calc):
        assert calculator.multiply(750, .5) == 375

class TestDivide:
    def test_divide_two_positive_ints_larger_numerator(self,calc):
        assert calculator.divide(14,7) == 2

    def test_divide_two_positive_ints_larger_denominator(self,calc):
        assert calculator.divide(7,14) == .5

    def test_divide_float_result(self,calc):
        assert calculator.divide(9,5) == pytest.approx(1.8)

    def test_divide_one_positive_one_negative_negative_numerator(self,calc):
        assert calculator.divide(-14,7) == -2

    def test_divide_one_positive_one_negative_positive_numerator(self,calc):
        assert calculator.divide(14,-7) == -2

    def test_divide_two_negative_ints(self,calc):
        assert calculator.divide(-14,-7) == 2

    def test_divide_num_by_zero_raises_error(self,calc):
        with pytest.raises(ZeroDivisionError, match="You can't divide by zero!"):
            calculator.divide(7,0)

    def test_divide_zero_by_zero_raises_error(self,calc):
        with pytest.raises(ZeroDivisionError, match="You can't divide by zero!"):
            calculator.divide(0,0)

    def test_divide_floats_with_float_result(self,calc):
        assert calculator.divide(6.7,4.2) == pytest.approx(1.59523809524)

    def test_divide_floats_with_int_result(self,calc):
        assert calculator.divide(8.4,4.2) == 2

    def test_divide_boundary_value_large_numerator(self,calc):
        assert calculator.divide(2222222222222,2) == 1111111111111

    def test_divide_boundary_value_large_denominator(self,calc):
        assert calculator.divide(2,1111111111111) == pytest.approx(.0000000000018)

    def test_divide_float_by_decimal_for_large_result(self,calc):
        assert calculator.divide(4.2,.0000000000067) == pytest.approx(626865671642)

class TestPower:
    def test_power_two_positive_ints(self,calc):
        assert calculator.power(2,4) == 16

    def test_power_one_postive_one_negative_int(self,calc):
        assert calculator.power(4,-2) == pytest.approx(.0625)

    def test_power_two_negative_ints(self,calc):
        assert calculator.power(-2,-2) == pytest.approx(.25)

    def test_power_two_positve_floats(self,calc):
        assert calculator.power(3.14,3.14) == pytest.approx(36.337838880175)

    def test_power_int_raised_to_a_float(self,calc):
        assert calculator.power(100,.25) == pytest.approx(3.1622776601684)

    def test_power_float_raised_to_an_int(self,calc):
        assert calculator.power(.99,20) == pytest.approx(.81790693759723)

    def test_power_zero_raised_to_num(self,calc):
        assert calculator.power(0,20) == 0

    def test_power_num_raised_to_zero(self,calc):
        assert calculator.power(100,0) == 1

    def test_power_zero_raised_to_zero_raises_error(self,calc):
        with pytest.raises(ValueError, match="Erm actually in high level contexts zero raised to the power of zero is undefined!"):
            calculator.power(0,0)

    def test_power_boundary(self,calc):
        assert calculator.power(100,5) == 10000000000

class TestSqrt:
    def test_sqrt_int_input_int_result(self,calc):
        assert calculator.square_root(64) == 8

    def test_sqrt_int_input_float_result(self,calc):
        assert calculator.square_root(55) == pytest.approx(7.4161984871)

    def test_sqrt_zero(self,calc):
        assert calculator.square_root(0) == 0

    def test_sqrt_negative_number_raises_error(self,calc):
        with pytest.raises(ValueError, match="You can't take the square root of a negative number!"):
            calculator.square_root(-64)
        
    def test_sqrt_float_input_float_result(self,calc):
        assert calculator.square_root(6.4) == pytest.approx(2.52982212813)

    def test_sqrt_boundary(self,calc):
        assert calculator.square_root(22222222222222) == pytest.approx(4714045.20791)

class TestMod:
    def test_mod_two_positive_ints_no_remainder(self,calc):
        assert calculator.modulus(6,2) == 0

    def test_mod_two_positive_ints_bigger_numerator(self,calc):
        assert calculator.modulus(6,4) == 2

    def test_mod__two_positive_ints_bigger_denominator(self,calc):
        assert calculator.modulus(4,6) == 4

    def test_mod_negative_numerator_positive_denominator(self,calc):
        assert calculator.modulus(-4,6) == 2

    def test_mod_positve_numberator_negative_denominator(self,calc):
        assert calculator.modulus(4,-6) == -2

    def test_mod_two_negative_ints(self,calc):
        assert calculator.modulus(-4,-6) == -4

    def test_mod_zero_by_num(self,calc):
        assert calculator.modulus(0,4) == 0

    def test_mod_with_a_zero_denominator_raises_error(self,calc):
        with pytest.raises(ZeroDivisionError, match="You can't divide by zero!"):
            calculator.modulus(4,0)

    def test_mod_with_a_zero_denominator_and_numerator_raises_error(self,calc):
        with pytest.raises(ZeroDivisionError, match="You can't divide by zero!"):
            calculator.modulus(0,0)

    def test_mod_two_floats(self,calc):
        assert calculator.modulus(6.4,2.4) == pytest.approx(1.6)

    def test_mod_boundary_big_numerator_small_denominator(self,calc):
        assert calculator.modulus(2222222222222,2) == 0

    def test_mod_boundary_big_numerator_big_denominator(self,calc):
        assert calculator.modulus(2222222222222,1111111111111) == 0

class TestFloorDivide:
    def test_floor_divide_two_positive_ints_no_round(self,calc):
        assert calculator.floor_divide(14, 2) == 7

    def test_floor_divide_larger_numerator(self,calc):
        assert calculator.floor_divide(14,5) == 2

    def test_floor_divide_larger_denominator(self,calc):
        assert calculator.floor_divide(5,14) == 0

    def test_floor_divide_negative_numerator_positive_denominator(self,calc):
        assert calculator.floor_divide(-14,7) == -2

    def test_floor_divide_positive_numerator_negative_denominator(self,calc):
        assert calculator.floor_divide(-14,-7) == 2

    def test_floor_divide_two_negative_ints(self,calc):
        assert calculator.floor_divide(-14,-7) == 2

    def test_floor_divide_zero_by_num(self,calc):
        assert calculator.floor_divide(0,7) == 0

    def test_floor_divide_num_by_zero_raises_error(self,calc):
        with pytest.raises(ZeroDivisionError, match="You can't divide by zero!"):
            calculator.floor_divide(7,0)

    def test_floor_divide_zero_by_zero_raises_error(self,calc):
        with pytest.raises(ZeroDivisionError, match="You can't divide by zero!"):
            calculator.floor_divide(0,0)

    def test_floor_divide_two_floats(self,calc):
        assert calculator.floor_divide(6.7,4.2) == 1
    
    def test_floor_divide_boundary(self,calc):
        assert calculator.floor_divide(2222222222222,1111111111111) == 2

class TestIntegration:

    def test_integration_add_and_subtract(self,calc):
        assert calculator.add(calculator.subtract(10,5), calculator.subtract(27,20)) == 12

    def test_integration_add_and_multiply(self,calc):
        assert calculator.add(calculator.multiply(10,2), calculator.multiply(-5,4)) == 0

    def test_integration_add_and_divide(self,calc):
        assert calculator.add(calculator.divide(100,5),calculator.divide(70,2)) == 55

    def test_integration_add_and_power(self,calc):
        assert calculator.add(calculator.power(2,2),calculator.power(3,3)) == 31

    def test_integration_add_and_square_root(self,calc):
        assert calculator.add(calculator.square_root(64),calculator.square_root(144)) == 20

    def test_integration_add_and_modulus(self,calc):
        assert calculator.add(calculator.modulus(78,12),calculator.modulus(99,9)) == 6

    def test_integration_add_and_floor_divide(self,calc):
        assert calculator.add(calculator.floor_divide(6789,1234),calculator.floor_divide(999999,444444)) == 7

    def test_integration_subtract_and_multiply(self,calc):
        assert calculator.subtract(calculator.multiply(10,4),calculator.multiply(-5,6)) == 70

    def test_integration_subtract_and_divide(self,calc):
        assert calculator.subtract(calculator.divide(10,2),calculator.divide(48,6)) == -3

    def test_integration_subtract_and_power(self,calc):
        assert calculator.subtract(calculator.power(10,2),calculator.power(3,4)) == 19

    def test_integration_subtract_and_square_root(self,calc):
        assert calculator.subtract(calculator.square_root(36),calculator.square_root(49)) == -1

    def test_integration_subtract_and_modulus(self,calc):
        assert calculator.subtract(calculator.modulus(78,12),calculator.modulus(99,7)) == 5

    def test_integration_subtract_and_floor_divide(self,calc):
        assert calculator.subtract(calculator.floor_divide(6789,1234), calculator.floor_divide(999999,444444)) == 3

    def test_integration_multiply_and_divide(self,calc):
        assert calculator.multiply(calculator.divide(10,2),calculator.divide(50,5)) == 50

    def test_intergration_multiply_and_power(self,calc):
        assert calculator.multiply(calculator.power(2,2),calculator.power(2,3)) == 32

    def test_intergration_multiply_and_square_root(self,calc):
        assert calculator.multiply(calculator.square_root(64),calculator.square_root(64)) == 64

    def test_integration_multiply_and_modulus(self,calc):
        assert calculator.multiply(calculator.modulus(78,12),calculator.modulus(78,12)) == 36

    def test_integration_multiply_and_floor_divide(self,calc):
        assert calculator.multiply(calculator.floor_divide(100,3),calculator.floor_divide(100,33)) == 99

    def test_integration_power_and_square_root(self,calc):
        assert calculator.power(calculator.square_root(64),calculator.square_root(36)) == 262144
    
    def test_integration_power_and_modulus(self,calc):
        assert calculator.power(calculator.modulus(3,2),calculator.modulus(99,9)) == 1
    
    def test_integration_power_and_floor_divide(self,calc):
        assert calculator.power(calculator.floor_divide(100,44),calculator.floor_divide(100,44)) == 4
    
    def test_integration_square_root_and_modulus(self,calc):
        assert calculator.square_root(calculator.modulus(350,21)) == pytest.approx(3.74165738677)

    def test_integration_square_root_and_floor_divide(self,calc):
        assert calculator.square_root(calculator.floor_divide(100,6)) == 4
    
    def test_integration_modulus_and_floor_divide(self,calc):
        assert calculator.modulus(calculator.floor_divide(100,6),calculator.floor_divide(100,12)) == 0

class TestGeorgia:
    def test_georgia_success(self,calc):
        assert calculator.add("Geo","rgia") == "Georgia"
