class Account:
    def __init__(self, client) -> None:
        self.client = client

    def create(self, data):
        url = "users/accounts"
        response = self.client.post(url_path=url, data=data)
        return response

    def update(self, uid, data):
        url = f"users/accounts/{int(uid)}"
        response = self.client.put(url_path=url, data=data)
        return response

    def list(self, offset, page):
        url = f"users/accounts?offset={int(offset)}&page={int(page)}"
        response = self.client.get(url_path=url)
        return response

    def accountDetails(self, uid):
        url = f"users/accounts/{int(uid)}"
        response = self.client.get(url_path=url)
        return response

    def delete(self, uid):
        url = f"users/accounts/{int(uid)}"
        response = self.client.delete(url_path=url)
        return response


class Contact:
    def __init__(self, client) -> None:
        self.client = client

    def createContact(self, data):
        url = "users/contacts"
        response = self.client.post(url_path=url, data=data)
        return response

    def contactDetail(self, uid):
        url = f"users/contacts/{int(uid)}"
        response = self.client.get(url_path=url)
        return response

    def listContact(self, offset, page):
        url = f"users/contacts?offset={int(offset)}&page={int(page)}"
        response = self.client.get(url_path=url)
        return response

    def updateContact(self, data, uid):
        url = f"users/contacts/{str(uid)}"
        response = self.client.put(url_path=url, data=data)
        return response

    def deleteContact(self, uid):
        url = f"users/contacts/{int(uid)}"
        response = self.client.delete(url_path=url)
        return response


class Transfer:
    def __init__(self, client) -> None:
        self.client = client

    def calculateCommission(self, amount):
        url = "users/transfers/commission"
        response = self.client.post(url_path=url, data=amount)
        return response

    def createPayment(self, data):
        url = "users/transfers"
        response = self.client.post(url_path=url, data=data)
        return response


    def paymentDetail(self, uid):
        url = f"users/transfers/{int(uid)}"
        response = self.client.get(url_path=url)
        return response

    def listTransfer(self, offset, page):
        url = f"users/transfers?offset={int(offset)}&page={int(page)}"
        response = self.client.get(url_path=url)
        return response

    def updateTransfer(self, data, uid):
        url = f"users/transfers/{int(uid)}"
        response = self.client.put(url_path=url, data=data)
        return response

    def deleteTransfer(self, uid):
        url = f"users/transfers/{int(uid)}"
        response = self.client.delete(url_path=url)
        return response


class PaymentAggregation:
    def __init__(self, client) -> None:
        self.client = client

    def commission(self, data):
        url = "users/aggregations/commission"
        response = self.client.post(url_path=url, data=data)
        return response

    def create(self, data):
        url = "users/aggregations"
        response = self.client.post(url_path=url, data=data)
        return response

    def details(self, uid):
        url = f"users/aggregations/{int(uid)}"
        response = self.client.get(url_path=url)
        return response

    def list(self, offset, page):
        url = f"users/aggregations?offset={int(offset)}&page={int(page)}"
        response = self.client.get(url_path=url)
        return response

    def update(self, data, uid):
        url = f"users/aggregations/{int(uid)}"
        response = self.client.put(url_path=url, data=data)
        return response

    def delete(self, uid):
        url = f"users/aggregations/{int(uid)}"
        response = self.client.delete(url_path=url)
        return response


class InvoiceTransfer:
    def __init__(self, client) -> None:
        self.client = client

    def calculateCommissionInvoice(self, amount):
        url = "users/invoices/commission"
        response = self.client.post(url_path=url, data=data)
        return response

    def createInvoice(self, data):
        url = "users/invoices"
        response = self.client.post(url_path=url, data=data)
        return response

    def InvoiceDetail(self, uid):
        url = f"users/invoices/{int(uid)}"
        response = self.client.get(url_path=url)
        return response

    def listInvoice(self, offset, page):
        url = f"users/invoices?offset={int(offset)}&page={int(page)}"
        response = self.client.get(url_path=url)
        return response

    def updateInvoice(self, data, uid):
        url = f"users/invoices/{str(uid)}"
        response = self.client.put(url_path=url, data=data)
        return response

    def deleteInvoice(self, uid):
        url = f"users/invoices/{int(uid)}"
        response = self.client.delete(url_path=url)
        return response
