# PyL — índice de las fuentes en texto

Cada `.md` es el texto de un archivo de `C:\Users\Fran\Desktop\SISTEMAS 3\PYL\`, con la misma
ruta. Las diapositivas (`.ppt`/`.pptx`) y los `.doc` se pasaron a PDF con PowerPoint y Word y de
ahí a texto con `fuentes/extraer.py`. Los dibujos de las diapositivas no tienen texto: para verlos,
convertir el `.ppt` a PDF otra vez y `python fuentes/pagina.py "<PDF>" N`.

| Tema | Archivo | Qué es |
| :-- | :-- | :-- |
| Base | `TOPIC 1/Traductores-Compiladores.md` | Evolución y clasificación de lenguajes, traductores, compilador e intérprete, fases de la compilación |
| Base | `TOPIC 1/Analisis_Lexico-Automatas_Finitos-Parte_1.md` | Análisis léxico (componente léxico, lexema, patrón), alfabeto, cadena, operaciones, lenguaje, AF (5-upla), diagrama y tabla, estado muerto, lenguaje reconocido |
| Base | `TOPIC 1/Practica_I_-_AutomatasER.md` | Trabajo Práctico I: 80 lenguajes para hacer AF y ER (el ejercicio 3 de los parciales sale de acá; el 80 es el del recuperatorio 2023) |
| ER | `TOPIC 2/Analisis_Lexico-Automatas_Finitos-Expresiones_Regulares-Parte_2.md` | Expresiones regulares (definición, prioridades) y AF → ER por eliminación de estados (p. 7: la regla α β* γ es un dibujo) |
| ER | `TOPIC 2/Analisis_Lexico-Automatas_Finitos-Expresiones_Regulares-Parte_3.md` | ER → AFN-ε (Thompson, p. 3 son dibujos), AFN-ε → AFD (subconjuntos), minimización |
| ER | `TOPIC 2/4 - Analisis Lexico-Automatas Finitos-Expresiones Regulares-Parte 3.md` | Otra copia del anterior (cambia solo el formato del título) |
| ER | `TOPIC 2/Analisis_Lexico-Automatas_Finitos-Parte_3.md` | De un AFD a un programa reconocedor en Pascal y armado de un analizador léxico (no lo toman los parciales) |
| Funcional | `TOPIC 3/*.md` | Programación funcional: teoría y práctica 2020. No entra en el parcial de autómatas; todavía no está en el campus |
| Exámenes | `Examenes/parcial paradigma 2023.md` y `recuperatorios parcial paradigma 2023.md` | Los dos de 2023 (el autómata del ejercicio 1 es un dibujo: ver el PDF) |

Los dos de 2025 son fotos (`Examenes/Parcial 2025.png`, `Recu 2025.png`): no tienen texto.
Los autómatas de los cuatro exámenes están pasados a `fuentes/pyl/diagramas/evaluacion.py`.
