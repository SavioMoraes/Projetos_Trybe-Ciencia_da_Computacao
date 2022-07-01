class TrackOrders:
    def __init__(self):
        self.orders = list()

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])
        print(self.orders)
        return self.orders

    def get_most_ordered_dish_per_customer(self, customer):
        most_request_dish = self.orders[0][1]
        frequency = {}
        for order in self.orders:
            if order[0] == customer:
                if order[1] not in frequency:
                    frequency[order[1]] = 1
                else:
                    frequency[order[1]] += 1

                if frequency[order[1]] > frequency[most_request_dish]:
                    most_request_dish = order[1]
        return most_request_dish

    def get_never_ordered_per_customer(self, customer):
        order_options = set()
        customer_orders = set()
        for client, dish, day in self.orders:
            order_options.add(dish)
            if client == customer:
                customer_orders.add(dish)
        customer_did_not_ask = order_options.difference(customer_orders)
        return customer_did_not_ask

    def get_days_never_visited_per_customer(self, customer):
        operating_days = set()
        days_the_customer_attended = set()
        for name, dish, day in self.orders:
            operating_days.add(day)
            if name == customer:
                days_the_customer_attended.add(day)
        days_the_customer_did_not_show_up = operating_days.difference(
            days_the_customer_attended
        )
        return days_the_customer_did_not_show_up

    def get_busiest_day(self):
        most_frequent_day = self.orders[0][2]
        frequency = {}
        for day in self.orders:
            if day[2] not in frequency:
                frequency[day[2]] = 1
            else:
                frequency[day[2]] += 1

            if frequency[day[2]] > frequency[most_frequent_day]:
                most_frequent_day = day[2]
        return most_frequent_day

    def get_least_busy_day(self):
        less_frequented_day = self.orders[0][2]
        frequency = {}
        for day in self.orders:
            if day[2] not in frequency:
                frequency[day[2]] = 1
            else:
                frequency[day[2]] += 1

            if frequency[day[2]] < frequency[less_frequented_day]:
                less_frequented_day = day[2]
        return less_frequented_day


if __name__ == "__main__":
    orders_len = TrackOrders()
    print(orders_len)
