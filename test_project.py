from meal_planner import user_list, breakfast, lunch, dinner
import pytest

userlist = {}
user = "Bob"

def test_user_list(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    user_list(userlist, user)
    assert user in userlist

def test_breakfast(monkeypatch):
    Eggs = ["Sunny-Side Up","Boiled Eggs", "Crispy Fried Eggs", "Fluffy Scrambled Eggs"]
    Meat = ["Ham and sausage", "Ham and bacon", "Steak", "Sardines on bread"]

    monkeypatch.setattr('builtins.input', lambda _: "1")
    selected_breakfast = breakfast(user, userlist)
    assert any(egg in selected_breakfast for egg in Eggs)

    monkeypatch.setattr('builtins.input', lambda _: "2")
    selected_breakfast = breakfast(user, userlist)
    assert any(meat in selected_breakfast for meat in Meat)

def test_lunch(monkeypatch):
    Sandwiches = ["Basil Chicken Sandwiches", "Salad Sandwiches", "Sausage and Pepper Sandwiches", "Shrimp Sandwiches"]
    Burgers = ["Chicken Burger", "Fish Burger", "Pork Burger", "Vegetarian Burger"]

    monkeypatch.setattr('builtins.input', lambda _: "1")
    selected_lunch = lunch(user, userlist)
    assert any(sandwiches in selected_lunch for sandwiches in Sandwiches)

    monkeypatch.setattr('builtins.input', lambda _: "2")
    selected_lunch = lunch(user, userlist)
    assert any(burger in selected_lunch for burger in Burgers)

def test_dinner(monkeypatch):
    Rice = ["Chicken Rice", "Coconut Rice", "Risotto", "Nasi Lemak"]
    Noodles = ["Spaghetti", "Laksa", "Pan Fried Noodles", "Ramen"]

    monkeypatch.setattr('builtins.input', lambda _: "1")
    selected_dinner = dinner(user, userlist)
    assert any(rice in selected_dinner for rice in Rice)

    monkeypatch.setattr('builtins.input', lambda _: "2")
    selected_dinner = dinner(user, userlist)
    assert any(noodle in selected_dinner for noodle in Noodles)
