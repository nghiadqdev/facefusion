from typing import List, Optional

import gradio

from facefusion import config, state_manager, translator
from facefusion.uis import choices as uis_choices

COMMON_OPTIONS_CHECKBOX_GROUP : Optional[gradio.Checkboxgroup] = None
SAVE_SETTINGS_BUTTON : Optional[gradio.Button] = None


def render() -> None:
	global COMMON_OPTIONS_CHECKBOX_GROUP
	global SAVE_SETTINGS_BUTTON

	common_options = []

	if state_manager.get_item('keep_temp'):
		common_options.append('keep-temp')

	COMMON_OPTIONS_CHECKBOX_GROUP = gradio.Checkboxgroup(
		label = translator.get('uis.common_options_checkbox_group'),
		choices = uis_choices.common_options,
		value = common_options
	)
	SAVE_SETTINGS_BUTTON = gradio.Button(
		value = 'Save settings',
		variant = 'secondary',
		size = 'sm'
	)


def listen() -> None:
	COMMON_OPTIONS_CHECKBOX_GROUP.change(update, inputs = COMMON_OPTIONS_CHECKBOX_GROUP)
	SAVE_SETTINGS_BUTTON.click(save)


def update(common_options : List[str]) -> None:
	keep_temp = 'keep-temp' in common_options
	state_manager.set_item('keep_temp', keep_temp)


def save() -> None:
	config.save_config()
