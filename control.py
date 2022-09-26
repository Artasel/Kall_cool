from operator import truediv
import UI as ui
import expression as exp
import complex_number as cnum
import check as ch
import real_number as rnum
import loger as log


def button_click():
    num1 = 0
    num2 = 0
    action = ''
    rez = ''
    proverka = False

    log.dif_log('Запуск программы.')
    ui.print('Приветсвуем Вас в программе калькулятор!!!\n')

    while True:

        rez = ui.input(
            'С какими числами хотите работать\n(1 - рациональными или 2 - комплексными числами или 3 - выход): ')
        log.dif_log(f'Выбранный режим работы - {rez}')

        # тут нужна проерка что введено 1 или 2

        proverka = ch.user_mode(rez)

        if not proverka:
            st = 'Режим работы выбран не верно'
            log.dif_log(st)
            ui.print(st)
            continue

        if int(rez) == 1:  # обрабатываем рациональные числа
            '''
            Вариант №1
            '''
            while True:  # обрабатываем первое число
                num1 = ui.input('Введите первое число')
                log.dif_log(f'Введено первое число: {num1}')
                proverka = ch.is_number(num1)
                if not proverka:
                    st = 'Первое число введено не верно. Попробуйте еще раз...'
                    log.dif_log(st)
                    ui.print(st)
                    continue
                break

            while True:  # обрабатываем второе число
                num2 = ui.input('Введите второе число')
                log.dif_log(f'Введено второе число: {num2}')
                proverka = ch.is_number(num2)
                if not proverka:
                    st = 'Второе число введено не верно. Попробуйте еще раз...'
                    log.dif_log(st)
                    ui.print(st)
                    continue
                break

            while True:  # обрабатываем знак
                action = ui.input(
                    'Что Вы хотите сделать с этими числами? (+,-,*,/)')
                log.dif_log(f'Введено действие с числами: {action}')
                proverka = ch.is_action(action)
                if not proverka:
                    st = 'Вводить можно только: +,-,*,/. Попробуйте еще раз...)'
                    log.dif_log(st)
                    ui.print(st)
                    continue
                break

            if action == '+':

                rez = rnum.sum_num(num1, num2)

            elif action == '-':

                rez = rnum.sub_num(num1, num2)

            elif action == '*':

                rez = rnum.mult_num(num1, num2)

            elif action == '/':

                rez = rnum.div_num(num1, num2)

            ui.print(f'Ответ: {rez}')
            log.dif_log(f'Ответ: {rez}')

            '''
            Вариант №2
            '''

            # while True:  # обрабатываем выражение
            #     t_queue = ui.input('Введите выражение')
            #     log.dif_log(f'Введено выражение: {t_queue}')

            #     proverka = ch.empty_line()

            #     if not proverka:
            #         st = 'Введенное выражение не корректно. Попробуйте еще раз...'
            #         log.dif_log(st)
            #         ui.print(st)
            #         continue
            #     break

            # rez = exp.assembly_example(rez)

            # ui.print(f'Ответ: {rez}')
            # log.dif_log(f'Ответ: {rez}')

        elif int(rez) == 2:  # обрабатываем комплексные числа

            while True:  # обрабатываем первое число
                num1 = ui.input(
                    'Введите первое комплексное число (действительная и мнимая части разделяются пробелом):')
                log.dif_log(f'Введено первое комплексное число: {num1}')

                proverka = ch.is_compl(num1)
                if not proverka:
                    st = 'Первое комплексное число введено не верно. Попробуйте еще раз...'
                    log.dif_log(st)
                    ui.print(st)
                    continue
                break

            while True:  # обрабатываем второе число
                num2 = ui.input('Введите второе комплексное число')
                log.dif_log(
                    f'Введите второе комплексное число (действительная и мнимая части разделяются пробелом): {num2}')

                proverka = ch.is_compl(num2)
                if not proverka:
                    st = 'Второе число введено не верно. Попробуйте еще раз...'
                    log.dif_log(st)
                    ui.print(st)
                    continue
                break

            while True:  # обрабатываем знак
                action = ui.input(
                    'Что Вы хотите сделать с этими числами? (+,-,*,/)')
                log.dif_log(f'Введено действие с числами: {action}')

                proverka = ch.is_action(action)
                if not proverka:
                    st = 'Вводить можно только: +,-,*,/. Попробуйте еще раз...)'
                    log.dif_log(st)
                    ui.print(st)
                    continue
                break

            if action == '+':

                rez = cnum.sum_num(num1, num2)

            elif action == '-':

                rez = cnum.sub_num(num1, num2)

            elif action == '*':

                rez = cnum.mult_num(num1, num2)

            elif action == '/':

                rez = cnum.div_num(num1, num2)

            ui.print(f'Ответ: {rez}')
            log.dif_log(f'Ответ: {rez}')

        break


st = 'Работа программы завершена.'
log.dif_log(st)
ui.print(st)
exit
