from django.db import models


# Create your models here.


class Offer(models.Model):
    title = models.CharField(
        verbose_name="Title", max_length=65, blank=True, default="Budget Flight"
    )
    url = models.CharField(
        verbose_name="Avatar",
        max_length=500,
        blank=True,
        default="https://cdn.britannica.com/34/196734-050-B7C6624F/Beechcraft-Baron-airplane-landing-aircraft-travel.jpg?w=300",
    )
    description = models.CharField(
        verbose_name="Description",
        max_length=500,
        blank=True,
        default="Capital A Berhad, operating as AirAsia is a Malaysian multinational low-cost airline headquartered near Kuala Lumpur, Malaysia. It is the largest airline in Malaysia by fleet size and destinations. AirAsia operates scheduled domestic and international flights to more than 165 destinations spanning 25 countries",
    )
    depart = models.CharField(verbose_name="Depart", max_length=32, default="HCM")
    arrival = models.CharField(verbose_name="Arrival", max_length=32, default="HN")
    depart_time = models.DateTimeField(
        verbose_name="Departure Time", default="12/25/23 14:30"
    )  # 10/25/06 14:30
    available_at = models.DateTimeField(
        verbose_name="Available", default="12/20/23 14:30"
    )  # 10/25/06 14:30
    price = models.IntegerField(verbose_name="Price", max_length=16, default=0)
    feedback = models.CharField(
        verbose_name="Feedback", max_length=100, blank=True, default=""
    )
    favourite = models.CharField(
        verbose_name="Favourite", max_length=100, blank=True, default=""
    )
    status = models.CharField(
        verbose_name="Status",
        max_length=16,
        default="CREATED",
    )

    def __str__(self):
        return self.title


class User(models.Model):
    email = models.CharField(verbose_name="email", max_length=65)
    name = models.CharField(verbose_name="email", max_length=65, blank=True, default="")
    password = models.CharField(verbose_name="password", max_length=120)
    role = models.CharField(verbose_name="Role", max_length=16)

    def __str__(self):
        return self.name
