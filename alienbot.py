#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 09:25:38 2021

@author: oscarliu
"""

# importing regex and random libraries
import re
import random

class AlienBot:
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
  # random starter questions
  random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )
    
  def __init__(self):
    self.alienbabble = {'describe_planet_intent': r'.*\s*your planet.*',
                        'answer_why_intent': r'why\sare.*',
                        'cubed_intent': r'.*cube.*(\d+)'
                            }

  # Greeting(Initial step of a conversation)
  def greet(self):
    self.name = input("What is your name? \n")
    will_help = input("Hi {name}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet? \n".format(name=self.name))
    if will_help in self.negative_responses:
      print("Ok, have a nice Earth day!")
      return
    self.chat()
    
    
   # Ending a conversation by detecting exit commands
  def make_exit(self, reply):
    for words in self.exit_commands:
      if words in reply:
        print("Ok, have a nice Earth day!")
        return True

  # Normal chat functionality
  def chat(self):
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
      reply = input(self.match_reply(reply))
  
  #Reply matching functionality based on regex pattern matching to identify intent
  def match_reply(self, reply):
    for key,value in self.alienbabble.items():
      intent = key
      regex_pattern = value
      found_match = re.match(regex_pattern,reply)
      if found_match and intent == 'describe_planet_intent':
        return self.describe_planet_intent()
      elif found_match and intent == 'answer_why_intent':
        return self.answer_why_intent()
      elif found_match and intent == 'cubed_intent':
        return self.cubed_intent(found_match.groups()[0])
      else:
        return self.no_match_intent()
  
  #Responses based on "describe_planet" intent
  def describe_planet_intent(self):
    responses = ("My planet is a utopia of diverse organisms and species. ", 
                 "I am from Opidipus, the capital of Wayward Galaxies. ")
    return random.choice(responses)

  # Responses based on "why" intent
  def answer_why_intent(self):
    responses = ("I come in peace.", "I am here to collect data on your planet and its inhabitants. ", 
                 "I heard the coffee is good. ")
    return random.choice(responses)
       
  # Response to answer a "mathematical cubing" question with entity input using regex
  def cubed_intent(self, number):
    number = int(number)
    cubed_number = number ** 3
    return f"The cube of {number} is {cubed_number}. Isn't that cool? "

  # Responses if no mathced intent is found
  def no_match_intent(self):
    responses = ("Please tell me more. ", "Tell me more! ", "Why do you say that? ", 
                 "I see. Can you elaborate? ", "Interesting. Can you tell me more? ", 
                 "I see. How do you think? ", "Why? ", "How do you think I feel when you say that? ")
    return random.choice(responses)



