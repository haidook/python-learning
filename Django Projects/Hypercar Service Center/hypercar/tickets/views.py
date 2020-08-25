from django.views import View
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('/welcome/')


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tickets/welcome.html')


class MenuView(View):
    def get(self, request, *args, **kwargs):
        data = {
            'change_oil': 'Change oil',
            'inflate_tires': 'Inflate Tires',
            'diagnostic': 'Get diagnostic test',
        }
        context = {
            'data': data
        }
        return render(request, 'tickets/menu.html', context=context)




class ItemView(TemplateView):
    tickets = []
    ticket_no = 0
    waiting_time = 0
    print(f'{waiting_time=}')
    line_of_cars = {'oil': [],
                    'tires': [],
                    'diag': []}
    def calculate_waiting(self, service):
        if service == 'oil':
            self.waiting_time += (len(self.line_of_cars['oil']) * 2)
        elif service == 'tires':
            self.waiting_time += (len(self.line_of_cars['oil']) * 2) + \
                                 (len(self.line_of_cars['tires']) * 5)
        elif service == 'diag':
            self.waiting_time += (len(self.line_of_cars['oil']) * 2) + \
                                 (len(self.line_of_cars['tires']) * 5) + \
                                 (len(self.line_of_cars['diag']) * 30)
        return self.waiting_time

    def add_to_line(self, service):
        self.ticket_no += len(self.tickets) + 1
        self.tickets.append(self.ticket_no)
        self.waiting_time = self.calculate_waiting(service)
        self.line_of_cars[service].append(self.ticket_no)
        return self.ticket_no, self.waiting_time

    def get(self, request, *args, **kwargs):
        if args[0] == 'change_oil':
            self.add_to_line('oil')
            context = {
                'ticket': self.ticket_no,
                'time': self.waiting_time
            }
        elif args[0] == 'inflate_tires':
            self.add_to_line('tires')
            context = {
                'ticket': self.ticket_no,
                'time': self.waiting_time
            }
        elif args[0] == 'diagnostic':
            self.add_to_line('diag')
            context = {
                'ticket': self.ticket_no,
                'time': self.waiting_time
            }
        return render(request, 'tickets/ticket.html', context=context)


class ProcessingView(ItemView):
    @classmethod
    def next_number(cls, self):
        for x, y in self.line_of_cars.items():
            if len(y) > 0:
                cls.next_ticket = self.line_of_cars[x][0]
                self.line_of_cars[x].pop(0)
                break
            else:
                cls.next_ticket = 0
        return cls.next_ticket

    def get(self, request, *args, **kwargs):
        data = {
            'Change oil': len(self.line_of_cars['oil']),
            'Inflate tires': len(self.line_of_cars['tires']),
            'Get diagnostic': len(self.line_of_cars['diag']),
        }
        context = {
            'data': data
        }
        return render(request, 'tickets/processing.html', context=context)

    def post(self, request, *args, **kwargs):
        self.next_number(self)
        return HttpResponseRedirect('/processing')


class NextView(ProcessingView):
    def get(self, request, *args, **kwargs):
        try:
            return render(request, 'tickets/next.html', context={'ticket': self.next_ticket})
        except:
            return render(request, 'tickets/next.html', context={'ticket': 0})
