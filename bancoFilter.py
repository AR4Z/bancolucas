# -*- coding: utf-8 -*-
import telegram.ext


class FilterServices(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == 'Servicios'

filter_service = FilterServices()


class FilterNewAccount(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == 'Crear cuenta'

filter_new_account = FilterNewAccount()


class FilterDesactivateAccount(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == 'Desactivar cuenta'

filter_desactivate_account = FilterDesactivateAccount()


class FilterActivateAccount(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == 'Activar cuenta'

filter_activate_account = FilterActivateAccount()


class FilterTransfer(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == 'Tansferencia'

filter_transfer = FilterTransfer()


class FilterNumber(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text.isdigit()

filter_number = FilterNumber()


class FilterAddBalance(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == "Agregar Saldo"


filter_add_balance = FilterAddBalance()


class FilterGetBalance(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == "Ver saldo"

filter_get_balance = FilterGetBalance()


class FilterWithdraw(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == "Retirar"

filter_withdraw = FilterWithdraw()


class FilterAccount(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == "Info cuenta"

filter_account = FilterAccount()


class FilterTransfer(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == "Transferir"

filter_transfer = FilterTransfer()


class FilterReturn(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == "Menu Principal"

filter_return = FilterReturn()


class FilterShowTransfers(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == "Mis transferencias"

filter_show_transfers = FilterShowTransfers()


class FiltersTransfersEntries(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == "Recibidas"

filter_show_transfers_entries = FiltersTransfersEntries()


class FiltersTransferSends(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == "Enviadas"

filter_show_transfers_sends = FiltersTransferSends()


class FiltersShowWithDraws(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == "Mis retiros"

filter_show_withdraws = FiltersShowWithDraws()


class FiltersRecargar(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == "Recargar"

filter_recargar = FiltersRecargar()


class FiltersShowRecharges(telegram.ext.BaseFilter):
    def filter(self, message):
        return message.text == "Mis recargas"

filter_show_recharges = FiltersShowRecharges()