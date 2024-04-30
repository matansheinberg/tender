class TenderData:
    def __init__(self, link: str, number: int, area: str, city: str, neighborhood: str, amount_apartment: int, category,
                 target, book_published: bool, publish_date, open_date, last_date):
        self.link = link
        self.number = number
        self.area = area
        self.city = city
        self.neighborhood = neighborhood
        self.amount_apartment = amount_apartment
        self.category = category
        self.target = target
        self.book_published = book_published
        self.publish_date = publish_date
        self.open_date = open_date
        self.last_date = last_date

    def __str__(self):
        return "link: " + self.link + "\nnumber: " + str(self.number) + "\narea: " + self.area + "\ncity: " + \
               self.city + "\nneighborhood: " + self.neighborhood + "\namount_apartment: " + \
               str(self.amount_apartment) + "\ncategory: " + self.category + "\ntarget: " + self.target + \
               "\nis book published: " + str(self.book_published) + "\ndates of publish-open-last: " + \
               self.publish_date + "-" + self.open_date + "-" + self.last_date + "\n"

    def __repr__(self):
        return self.__str__()

    def get_link(self):
        return self.link

    def get_number(self):
        return self.number

    def get_area(self):
        return self.area

    def get_city(self):
        return self.city

    def get_neighborhood(self):
        return self.neighborhood

    def get_amount_apartment(self):
        return self.amount_apartment

    def get_category(self):
        return self.category

    def get_target(self):
        return self.target

    def get_book_published(self):
        return self.book_published

    def get_publish_date(self):
        return self.publish_date

    def get_open_date(self):
        return self.open_date

    def get_last_date(self):
        return self.last_date

    def get_data(self):
        return [self.link, self.number, self.area, self.city, self.neighborhood,
                self.amount_apartment, self.category, self.target, self.book_published,
                self.publish_date, self.open_date, self.last_date]
