class InvoiceTransferMerchant:
    def __init__(self, client) -> None:
        self.client = client

    def createInvoice(self, data):
        url = "merchants/invoices"
        response = self.client.post(url_path=url, data=data)
        return response

    def invoiceDetail(self, uid):
        url = f"invoices/{int(uid)}"
        response = self.client.get(url_path=url)
        return response

    def listInvoice(self, offset, page):
        url = f"merchants/invoices?offset={int(offset)}&page={int(page)}"
        response = self.client.get(url_path=url)
        return response

    def updateInvoice(self, data, uid):
        url = f"merchants/invoices/{int(uid)}"
        response = self.client.put(url_path=url, data=data)
        return response

    def deleteInvoice(self, uid):
        url = f"merchants/invoices/{int(uid)}"
        response = self.client.delete(url_path=url)
        return response
