# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 18:23:17 2017

@author: Arina
A simple desktop application that checks the knowledge of words 
from a given vocabulary file.
"""

#!/usr/bin/env python
import re, os, sys
import tkinter as tk

class Vocabulary(object):   
    """Representation of vocabulary that is stored in the file."""
    
    def __init__(self, file):
        """Creates dictionary with entries in the form 
        {word: (unit, definition)} from vocabulary file."""
        self.file = file
        self.definitions = {}
        f = open(self.file, mode='r', encoding='utf-8')
        lines = [line for line in f]
        for line in lines:
            if re.match('[0-9]+', line):
                last_unit = line[:-1]
            elif line == '\n':
                continue
            else:
                word_definition = line.split('=')
                self.definitions[word_definition[0].strip()] = (last_unit, word_definition[1].strip())
    
    def show_word(self):
        """Gets the next word from the dictionary."""
        for word, definition in self.definitions.items():
            yield (word.upper(), definition)


class Check(object):
    """Represents a mechanism to check if the given definition is the correct 
    definition of the given word."""
    
    def __init__(self, definition, input_definition):
        """Input is a String, definition is a tuple of Strings: (unit, definition)"""
        self.definition = definition[1].lower()
        self.unit = definition[0]
        self.input = input_definition.lower()
    
    def check_word_definition(self):
        """Checks if the definition is the correct definition of the word.
        Returns "Correct!..." if the input definition matched word's 
        defintion, "Correct! + definition" if the input matched only partially,
        otherwise returns "Incorrect. Answer: " ..."""
        if self.input == self.definition:
            return "Correct!" + "\nWord from unit #" + self.unit
        elif self.input in self.definition and self.input != "" and \
            (self.definition.count(" ") < 4 or (self.definition.count(",") > 0 or self.definition.count(";") > 0)):
            return "Correct!\n" + self.definition.upper() + "." + "\nWord from unit #" + self.unit
        else:
            return "Incorrect. Answer: " + self.definition.upper() + "." + "\nWord from unit #" + self.unit

        
class GUI(object):
    """Graphical representation and counters of correct, incorrect and total
    number of answers."""
    
    count_words = 0
    count_correct = 0
    
    def __init__(self, master, file):
        """Initiates the form."""
        
        self.vocab = Vocabulary(file).show_word()
        self.definition = None
        
        master.minsize(width=500, height=300) 
        master.maxsize(width=500, height=300)
        
        self.word = tk.Message(master, text='Click "Start" to begin translating words.', width=400)
        self.word.grid(row=1, column=0, columnspan=5, pady=5)
        
        self.answer = tk.Text(master, width=50, height=2, relief=tk.GROOVE, borderwidth=3, state=tk.DISABLED)
        self.answer.grid(row=2, column=0, columnspan=5, pady=10)
        
        self.result = tk.Message(master, \
            text='Instructions:\n1. Type your answer into the box above.\n2. Click "Check" or press Return on the keyboard.'+\
            '\n3. Click "Next word" or press Left Arrow on the keyboard.\n4. Click "Finish" to finish and get your result.', width=400, justify=tk.CENTER)
        self.result.grid(row=3, column=0, columnspan=5)
        
        self.quit_button = tk.Button(master, text='Quit', command = master.quit, height=4, width=8)
        self.quit_button.grid(row=0, column=0, pady=5)
        
        self.finish_button = tk.Button(master, text='Finish', command=self.quit_translation, height=4, width=8)
        self.finish_button.grid(row=0, column=1, pady=5)
        
        self.check_button = tk.Button(master, text='Check', command=self.check, state=tk.DISABLED, height=4, width=8)
        self.check_button.grid(row=0, column=2, pady=5)
        
        self.next_button = tk.Button(master, text='Next word', command=self.run, state=tk.DISABLED, height=4, width=8)
        self.next_button.grid(row=0, column=3, pady=5)
        
        self.start_button = tk.Button(master, text='Start', command=self.run, height=4, width=8)
        self.start_button.grid(row=0, column=4, pady=5)
        
        master.bind("<Return>", lambda _: self.check())
        master.bind("<Right>", lambda _: self.run())
    
    def run(self):    
        """Produces next word to translate and updates total words counter."""
        self.answer.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)
        self.check_button.config(state=tk.ACTIVE)
        self.next_button.config(state=tk.ACTIVE)
        self.finish_button.config(state=tk.ACTIVE)
        self.result.config(text="")
        w = self.vocab.__next__()
        GUI.count_words += 1
        message = 'Translate: ' + w[0]
        self.word.config(text=message)
        self.definition = w[1]
        if GUI.count_words == 1:
            self.start_button.config(state=tk.DISABLED)
        elif GUI.count_words > 1:
            self.answer.delete(1.0, tk.END)
  
    def check(self):
        """Checks the input, shows the result and updates correct words counter."""
        ans = self.answer.get(1.0, tk.END)
        c = Check(self.definition, ans.strip())
        res = c.check_word_definition()
        self.result.config(text=res)
        if res[0:8] == "Correct!":
            GUI.count_correct += 1
    
    def quit_translation(self):
        """Shows the counters and then sets them to zero."""
        message = 'You have translated correctly ' + str(GUI.count_correct) + ' words out of ' + str(GUI.count_words) + '.\nClick "Quit" to quit or "Start" to start over.'
        self.word.config(text=message)
        self.result.config(text="")
        self.answer.delete(1.0, tk.END)
        self.answer.config(state=tk.DISABLED)
        self.start_button.config(state=tk.ACTIVE)
        self.check_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.DISABLED)
        self.finish_button.config(state=tk.DISABLED)
        GUI.count_correct = 0
        GUI.count_words = 0


window = tk.Tk()
window.title('Vocabulary Test')

filename = os.path.join(os.path.dirname(sys.executable), 'vocabulary.txt')
g = GUI(window, filename)

#g = GUI(window, 'vocabulary.txt')

window.mainloop()
window.destroy()