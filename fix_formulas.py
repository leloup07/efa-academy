#!/usr/bin/env python3
import re
import os

def latex_to_text(formula):
    """Convierte LaTeX a texto legible"""
    f = formula
    
    # Fracciones: \frac{a}{b} -> (a)/(b)
    while '\\frac{' in f:
        match = re.search(r'\\frac\{([^{}]*)\}\{([^{}]*)\}', f)
        if match:
            f = f[:match.start()] + f'({match.group(1)})/({match.group(2)})' + f[match.end():]
        else:
            break
    
    # Raíz cuadrada: \sqrt{x} -> √(x)
    f = re.sub(r'\\sqrt\{([^{}]*)\}', r'√(\1)', f)
    
    # Subíndices simples: x_1 -> x₁, x_i -> xᵢ
    subscripts = {'0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄', 
                  '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉',
                  'i': 'ᵢ', 'j': 'ⱼ', 'n': 'ₙ', 'm': 'ₘ', 'p': 'ₚ',
                  'A': 'ₐ', 'B': '᷾', 'f': 'f', 't': 'ₜ'}
    
    # Subíndices con llaves: _{AB} -> ₐ᷾
    def replace_subscript(match):
        content = match.group(1)
        result = ''
        for c in content:
            result += subscripts.get(c, c)
        return result
    f = re.sub(r'_\{([^{}]*)\}', replace_subscript, f)
    
    # Subíndices simples: _x -> ₓ
    def replace_simple_subscript(match):
        c = match.group(1)
        return subscripts.get(c, '_' + c)
    f = re.sub(r'_([0-9A-Za-z])', replace_simple_subscript, f)
    
    # Superíndices: ^2 -> ², ^n -> ⁿ
    superscripts = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
                    '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
                    'n': 'ⁿ', '-': '⁻', '+': '⁺', '(': '⁽', ')': '⁾'}
    
    def replace_superscript(match):
        content = match.group(1)
        result = ''
        for c in content:
            result += superscripts.get(c, c)
        return result
    f = re.sub(r'\^\{([^{}]*)\}', replace_superscript, f)
    
    def replace_simple_superscript(match):
        c = match.group(1)
        return superscripts.get(c, '^' + c)
    f = re.sub(r'\^([0-9n\-])', replace_simple_superscript, f)
    
    # Letras griegas
    greek = {
        '\\alpha': 'α', '\\beta': 'β', '\\gamma': 'γ', '\\delta': 'δ',
        '\\sigma': 'σ', '\\mu': 'μ', '\\rho': 'ρ', '\\lambda': 'λ',
        '\\pi': 'π', '\\omega': 'ω', '\\epsilon': 'ε', '\\theta': 'θ',
        '\\Sigma': 'Σ', '\\Delta': 'Δ', '\\Omega': 'Ω'
    }
    for latex, symbol in greek.items():
        f = f.replace(latex, symbol)
    
    # Símbolos matemáticos
    symbols = {
        '\\times': '×', '\\div': '÷', '\\pm': '±', '\\leq': '≤',
        '\\geq': '≥', '\\neq': '≠', '\\approx': '≈', '\\infty': '∞',
        '\\sum': 'Σ', '\\prod': 'Π', '\\int': '∫',
        '\\left(': '(', '\\right)': ')', '\\left[': '[', '\\right]': ']',
        '\\bar{R}': 'R̄', '\\bar{r}': 'r̄', '\\overline{R}': 'R̄',
        '\\ ': ' ', '\\,': ' ', '\\;': ' ', '\\quad': '  ',
        '\\text{': '', '\\mathrm{': '', '\\mathbf{': ''
    }
    for latex, symbol in symbols.items():
        f = f.replace(latex, symbol)
    
    # Limpiar llaves restantes de \text{} etc
    f = re.sub(r'\}', '', f)
    f = re.sub(r'\{', '', f)
    
    # Limpiar espacios múltiples
    f = re.sub(r'  +', ' ', f)
    
    return f.strip()

def process_file(filepath):
    """Procesa un archivo .md convirtiendo fórmulas LaTeX"""
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Encontrar y reemplazar fórmulas entre $$ ... $$
    def replace_formula(match):
        latex = match.group(1)
        converted = latex_to_text(latex)
        return f'**{converted}**'
    
    # Fórmulas en bloque $$...$$
    new_content = re.sub(r'\$\$([^$]+)\$\$', replace_formula, content)
    
    # Fórmulas inline $...$
    new_content = re.sub(r'\$([^$]+)\$', replace_formula, new_content)
    
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    return True

# Directorio de manuales
manuales_dir = os.path.expanduser('~/Projects/efa_academy/data/manuales')

if os.path.exists(manuales_dir):
    files = [f for f in os.listdir(manuales_dir) if f.endswith('.md')]
    print(f"Procesando {len(files)} archivos...")
    for filename in files:
        filepath = os.path.join(manuales_dir, filename)
        process_file(filepath)
        print(f"  ✓ {filename}")
    print(f"\n✅ {len(files)} manuales actualizados")
else:
    print(f"❌ No existe: {manuales_dir}")
