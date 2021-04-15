namespace php calculadora

exception CalculadoraException{
    1: string mensaje
}

service calculadora{
    i32 adicion(1: i32 num1, 2: i32 num2) throws (1: CalculadoraException calculadoraException),

    i32 substraccion(1: i32 minuendo, 2: i32 sustraendo) throws (1: CalculadoraException calculadoraException),

    i32 multiplicacion(1: i32 num1, 2: i32 num2) throws (1: CalculadoraException calculadoraException),

    double division(1: i32 dividendo,2: i32 divisor) throws (1: CalculadoraException calculadoraException)
}