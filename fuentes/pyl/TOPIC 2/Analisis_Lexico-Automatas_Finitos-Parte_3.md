# Analisis_Lexico-Automatas_Finitos-Parte_3

Fuente: `C:/Users/Fran/AppData/Local/Temp/claude/C--Users-Fran-Desktop-NewCampus/196b4912-5fa9-4a20-89f0-578e09e99c9b/scratchpad/pyl-pdf/TOPIC 2/Analisis_Lexico-Automatas_Finitos-Parte_3.pdf` · 5 página(s) · texto extraído con pypdf.
Primero este texto; el PDF solo en las páginas marcadas ⚠ o si algo no cierra.

| Pág. | Qué hay |
| :-- | :-- |
| 1 |  |
| 2 |  |
| 3 |  |
| 4 |  |
| 5 |  |

<!-- página 1 -->

1
Análisis Léxico, Lenguajes
Formales, Autómatas Finitos
Paradigmas y Lenguajes

<!-- página 2 -->

2
Lenguajes Formales, Autómatas Finitos,
Expresiones Regulares y Análisis Léxico
Transformación de un Autómata Finito Determinístico en un
programa de reconocedor (función)
Function EsIdentificador(Cadena:String):Boolean;
Const
q0=0;
F=[0];
Type
Q=0..2;
Sigma=(Letra, Digito, Otro);
TipoDelta=Array[Q,Sigma] of Q;
Var
Control:Integer;
EstadoActual:Q;
Delta:TipoDelta;
Begin
{Cargar la tabla de transiciones}
Delta[0,Letra]:=1;
Delta[0,Digito]:=2;
. . .
{Recorrer la cadena de entrada y cambiar estados}
EstadoActual:=q0;
For Control:=1 to Length(S) do
EstadoActual:=Delta[EstadoActual,CarASimb(Cadena[Control])];
EsIdentificador:=EstadoActual in F;
End;

<!-- página 3 -->

3
Lenguajes Formales, Autómatas Finitos,
Expresiones Regulares y Análisis Léxico
Función auxiliar que transforma un carácter de la cadena en un símbolo de S :
Function CarASimb(Car:Char):Sigma;
Begin
Case Car of
‘a’..‘z’, ‘A’..‘Z’:CarASimb:=Letra;
‘0’..‘9’ :CarASimb:=Digito;
else
CarASimb:=Otro
End;
End;
▪ De esta manera cualquier AFD se puede transformar en un programa similar. Solo hay que
cambiar los componentes del AFD (Estados, Símbolos, Función de Transición, Estado Inicial y
Estados Finales).
▪ Esto reduce el problema de crear un algoritmo de reconocimiento, al problema de crear un
Autómata para el lenguaje regular.

<!-- página 4 -->

4
Lenguajes Formales, Autómatas Finitos y
Análisis Léxico
Implementación de un Analizador Léxico mediante Autómatas Finitos:
1. Definir los Componentes Léxicos
2. Crear Automatas Finitos para cada Componente Léxico complejo y obtener el AFD Mínimo
3. Definir el procedimiento ObtenerSiguienteCompLex() que representa al Analizador Léxico, con la siguiente
estructura:
Procedure ObtenerSiguienteCompLex(Var Fuente:FileOfChar;Var Control:Longint;
Var CompLex:TipoComplex;Var Lexema:String;Var TS:TablaDeSimbolos);
. . .
Begin {La TAS ya ingresa cargada con las Palabras Reservadas}
{Avanzar el Control salteando todos los caracteres de control y espacios,
hasta el primer carácter significativo}
If EsIdentificador(Fuente,Control,Lexema) then
InstalarEnTAS(Lexema,TS,CompLex)
else If EsConstanteReal(Fuente,Control,Lexema) then
CompLex:=ConstanteReal
else If EsConstanteEntera(Fuente,Control,Lexema) then
CompLex:=ConstanteEntera
else . . .
else if Not EsSimboloEspecial(Fuente,Control,Lexema,CompLex) then
CompLex:=ErrorLexico
End;

<!-- página 5 -->

5
Lenguajes Formales y Autómatas Finitos
FIN
Lenguajes Regulares,
Autómatas Finitos,
Análisis Léxico
