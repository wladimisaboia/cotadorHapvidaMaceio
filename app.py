from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('cotacao.html')

@app.route('/cotacao', methods=['POST'])
def cotar():
    idades_str = request.form['idade']
    idades = [int(age.strip()) for age in idades_str.split(',')]
    plano = request.form['plano'].strip()

    valores = {}
    total_valor = 0
    desconto_aplicado = False

    for idade in idades:
        valor = 0

        if plano == 'ambulatorial (pessoa física) - Sem coparticipação, exceto terapias' or plano == 'ambulatorial (pessoa física) - Com coparticipação' or plano == 'nosso plano enfermaria (pessoa física) - Sem coparticipação, exceto terapias' or plano == 'nosso plano enfermaria (pessoa física) - Com coparticipação' or plano == 'nosso plano apartamento (pessoa física) - Sem coparticipação, exceto terapias' or plano == 'nosso plano apartamento (pessoa física) - Com coparticipação' or plano == 'mix enfermaria (pessoa física) - Sem coparticipação, exceto terapias' or plano == 'mix apartamento (pessoa física) - Sem coparticipação, exceto terapias':
            if len(idades) >= 2 and not desconto_aplicado:
                valor = valor * 0.95
                desconto_aplicado = True

        if plano == 'ambulatorial (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 239.06
            elif idade <= 23:
                valor = 314.95
            elif idade <= 28:
                valor = 359.15
            elif idade <= 33:
                valor = 400.74
            elif idade <= 38:
                valor = 421.78
            elif idade <= 43:
                valor = 473.62
            elif idade <= 48:
                valor = 579.35
            elif idade <= 53:
                valor = 803.85
            elif idade <= 58:
                valor = 1083.90
            else:
                valor = 1407.96
        elif plano == 'ambulatorial (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 142.20
            elif idade <= 23:
                valor = 188.13
            elif idade <= 28:
                valor = 214.84
            elif idade <= 33:
                valor = 239.98
            elif idade <= 38:
                valor = 252.70
            elif idade <= 43:
                valor = 284.03
            elif idade <= 48:
                valor = 337.94
            elif idade <= 53:
                valor = 483.64
            elif idade <= 58:
                valor = 652.91
            else:
                valor = 848.78
        elif plano == 'nosso plano enfermaria (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 321.21
            elif idade <= 23:
                valor = 422.81
            elif idade <= 28:
                valor = 484.81
            elif idade <= 33:
                valor = 543.52
            elif idade <= 38:
                valor = 570.51
            elif idade <= 43:
                valor = 644.19
            elif idade <= 48:
                valor = 785.10
            elif idade <= 53:
                valor = 1082.03
            elif idade <= 58:
                valor = 1459.44
            else:
                valor = 1896.16
        elif plano == 'nosso plano enfermaria (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 235.49
            elif idade <= 23:
                valor = 309.66
            elif idade <= 28:
                valor = 355.55
            elif idade <= 33:
                valor = 397.77
            elif idade <= 38:
                valor = 417.47
            elif idade <= 43:
                valor = 471.26
            elif idade <= 48:
                valor = 574.12
            elif idade <= 53:
                valor = 790.88
            elif idade <= 58:
                valor = 1066.39
            else:
                valor = 1385.19
        elif plano == 'nosso plano apartamento (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 479.95
            elif idade <= 23:
                valor = 632.35
            elif idade <= 28:
                valor = 726.55
            elif idade <= 33:
                valor = 813.40
            elif idade <= 38:
                valor = 853.88
            elif idade <= 43:
                valor = 964.40
            elif idade <= 48:
                valor = 1175.75
            elif idade <= 53:
                valor = 1621.13
            elif idade <= 58:
                valor = 2187.23
            else:
                valor = 2842.29
        elif plano == 'nosso plano apartamento (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 351.31
            elif idade <= 23:
                valor = 462.54
            elif idade <= 28:
                valor = 531.36
            elif idade <= 33:
                valor = 594.68
            elif idade <= 38:
                valor = 624.23
            elif idade <= 43:
                valor = 704.90
            elif idade <= 48:
                valor = 859.16
            elif idade <= 53:
                valor = 1184.23
            elif idade <= 58:
                valor = 1597.41
            else:
                valor = 2075.52
        elif plano == 'ambulatorial (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 229.73
            elif idade <= 23:
                valor = 257.30
            elif idade <= 28:
                valor = 288.18
            elif idade <= 33:
                valor = 331.41
            elif idade <= 38:
                valor = 381.12
            elif idade <= 43:
                valor = 453.53
            elif idade <= 48:
                valor = 566.91
            elif idade <= 53:
                valor = 708.64
            elif idade <= 58:
                valor = 1204.69
            else:
                valor = 1349.25
        elif plano == 'ambulatorial (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 135.49
            elif idade <= 23:
                valor = 151.75
            elif idade <= 28:
                valor = 169.96
            elif idade <= 33:
                valor = 195.45
            elif idade <= 38:
                valor = 224.77
            elif idade <= 43:
                valor = 267.48
            elif idade <= 48:
                valor = 334.35
            elif idade <= 53:
                valor = 417.94
            elif idade <= 58:
                valor = 710.50
            else:
                valor = 795.76
        elif plano == 'enfermaria (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 292.60
            elif idade <= 23:
                valor = 327.71
            elif idade <= 28:
                valor = 367.04
            elif idade <= 33:
                valor = 422.10
            elif idade <= 38:
                valor = 485.42
            elif idade <= 43:
                valor = 577.65
            elif idade <= 48:
                valor = 722.06
            elif idade <= 53:
                valor = 902.58
            elif idade <= 58:
                valor = 1534.39
            else:
                valor = 1718.52
        elif plano == 'enfermaria (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 210.09
            elif idade <= 23:
                valor = 235.30
            elif idade <= 28:
                valor = 263.54
            elif idade <= 33:
                valor = 303.07
            elif idade <= 38:
                valor = 348.53
            elif idade <= 43:
                valor = 414.75
            elif idade <= 48:
                valor = 518.44
            elif idade <= 53:
                valor = 648.05
            elif idade <= 58:
                valor = 1101.69
            else:
                valor = 1233.89
        elif plano == 'apartamento (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 438.23
            elif idade <= 23:
                valor = 490.82
            elif idade <= 28:
                valor = 549.72
            elif idade <= 33:
                valor = 632.18
            elif idade <= 38:
                valor = 727.01
            elif idade <= 43:
                valor = 865.14
            elif idade <= 48:
                valor = 1081.43
            elif idade <= 53:
                valor = 1351.79
            elif idade <= 58:
                valor = 2298.04
            else:
                valor = 2573.80
        elif plano == 'apartamento (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 314.34
            elif idade <= 23:
                valor = 352.06
            elif idade <= 28:
                valor = 394.31
            elif idade <= 33:
                valor = 453.46
            elif idade <= 38:
                valor = 521.48
            elif idade <= 43:
                valor = 620.56
            elif idade <= 48:
                valor = 775.70
            elif idade <= 53:
                valor = 969.63
            elif idade <= 58:
                valor = 1648.37
            else:
                valor = 1846.17
        else:
            return 'Plano inválido'

        if idade not in valores:
            valores[idade] = {'plano': [], 'qtd': 0}

        valores[idade]['plano'].append(valor)
        total_valor += valor
        valores[idade]['qtd'] += 1

    if desconto_aplicado:
        total_valor = total_valor * 0.95

    total_valor = '{:.2f}'.format(total_valor)

    return render_template('resposta.html', valores=valores, total_valor=total_valor, desconto_aplicado=desconto_aplicado, plano_selecionado=plano)

if __name__ == '__main__':
    app.run(debug=True)