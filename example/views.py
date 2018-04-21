# -*- coding: utf-8 -*-

from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def game_slider(request):
    return render(request, 'game_slider.html', {})


def standings(request):
    return render(request, 'standings.html', {})


def schedule(request):
    return render(request, 'schedule.html', {})


def game_report(request, gameId):
    return render(request, 'game_report.html', {'gameId': gameId})


def game_livebox(request, gameId):
    return render(request, 'game_livebox.html', {'gameId': gameId})


def game_playbyplay(request, gameId):
    return render(request, 'game_playbyplay.html', {'gameId': gameId})


def player_stats(request):
    return render(request, 'player_stats.html', {})


def team_fullpage(request, teamId):
    return render(request, 'team_fullpage.html', {'teamId': teamId})