#!/usr/bin/python3

from renderlib import *

# URL to Schedule-XML
scheduleUrl = 'https://eh15.easterhegg.eu/frab/en/eh15/public/schedule.xml'

# For (really) too long titles
titlemap = {
	#708: "Neue WEB-Anwendungen des LGRB Baden-Württemberg im Überblick"
}


def introFrames(parameters):
	# 5 Sekunden

	# 2 Sekunde Text Fadein
	frames = 2*fps
	for i in range(0, frames):
		yield (
			('text', 'style',    'opacity', "%.4f" % easeInCubic(i, 0, 1, frames)),
			('text', 'attr',     'transform', 'translate(%.4f, 0)' % easeOutCubic(i, 0, 30, frames)),
		)

	# 2 Sekunden stehen lassen
	frames = 2*fps
	for i in range(0, frames):
		yield ()

	# 2 Sekunde Text Fadeout
	frames = 2*fps
	for i in range(0, frames):
		yield (
			('text', 'style',    'opacity', "%.4f" % easeInCubic(i, 1, -1, frames)),
			('text', 'attr',     'transform', 'translate(%.4f, 0)' % easeInCubic(i, 30, 30, frames)),
		)

	# two final frames
	for i in range(0, 2):
		yield (
			('text', 'style',    'opacity', "%.4f" % 0),
			('text', 'attr',     'transform', 'translate(%.4f, 0)' % 30),
		)


def debug():
	render(
		'intro.svg',
		'../intro.dv',
		introFrames,
		{
			'$id': 5725,
			'$title': 'Sleep? Ain\'t nobody got time for that!',
			'$subtitle': 'Physiologie von Schlaf und Wachzustand',
			'$personnames': 'Christina'
		}
	)

	render(
		'intro.svg',
		'../intro.ts',
		introFrames,
		{
			'$id': 5725,
			'$title': 'Sleep? Ain\'t nobody got time for that!',
			'$subtitle': 'Physiologie von Schlaf und Wachzustand',
			'$personnames': 'Christina'
		}
	)

def tasks(queue):
	# iterate over all events extracted from the schedule xml-export
	for event in events(scheduleUrl):

		# generate a task description and put them into the queue
		queue.put(Rendertask(
			infile = 'intro.svg',
			outfile = str(event['id'])+".dv",
			sequence = introFrames,
			parameters = {
				'$id': event['id'],
				'$title': event['title'],
				'$subtitle': event['subtitle'],
				'$personnames': event['personnames']
			}
		))

		queue.put(Rendertask(
			infile = 'intro.svg',
			outfile = str(event['id'])+".ts",
			sequence = introFrames,
			parameters = {
				'$id': event['id'],
				'$title': event['title'],
				'$subtitle': event['subtitle'],
				'$personnames': event['personnames']
			}
		))
