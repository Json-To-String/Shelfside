import pandas as pd
import numpy as np
import streamlit as st

class Handler():

    def __init__(self):
        self.personas = ['Blue', 'Red', 'Clear', 'Black', 'White', 'Green',
                        'Yellow', 'Purple', 'Natural', 'Parchment']

        self.question_options = [
                                'Highly Disagree',
                                'Disagree',
                                'Slightly Disagree',
                                'Neutral',
                                'Slightly Agree',
                                'Agree',
                                'Highly Agree'
                                ]

        # self.question_values = [1, 2, 3, 4, 5, 6, 7]
        self.question_values = [-3, -2, -1, 0, 1, 2, 3]

        # creates dict = {options : values}
        self.question_mapping = dict(map(lambda i,j : (i,j),
                                self.question_options, self.question_values))

        self.question_dict = {}
        self.question_list = []

        ## playing with the idea of list of dictionaries for weights
        self.question_weights = []

        self.question_keys = []

        self.page_results = {persona: None for persona in self.personas}


    def get_questions(self, textfile):
        """
        Called when needing to access questions
        """

        with open(textfile, 'r') as q:

            for ind, line in enumerate(q):

                # Questions are on even indices in the .txt
                if ind % 2 == 0:
                    self.question_list.append(line)

                # weights are on odd indices

                # want to make ex question weight: {Blue : 3, Red: 0, ...}
                else:
                    # start weight dictionary using comprehension
                    weights = {persona: None for persona in self.personas}

                    # strip off parentheses
                    # text = line[1:-1]
                    text = line.replace('(', '').replace(')', '')

                    text = text.split(',')

                    for item in text:
                        item = item.split(' ')

                        # text after split on whitespace looks like:
                        # ['', 'Blue', '-2']
                        # ['', 'Red', '2']

                        color, number = str(item[1]), float(item[-1])
                        weights[color] = number

                    self.question_weights.append(weights)

        # creates dict = {question : weights}
        self.question_dict = dict(map(lambda i,j : (i,j),
                                self.question_list, self.question_weights))

    def display_questions(self, page_num):

    # with st.form('page_form'):
    ## Main Question Loop
        for i in range(len(self.question_list)):
            quest = self.question_list[i]
            # weight = self.question_weights[i]

            quest_key = f'page{page_num}_question{i}'

            # self.question_keys.append(quest_key) ## potentiall superfluous

            answer = st.radio(f'{quest}',
                                self.question_options,
                                horizontal = False,
                                key = quest_key,
                                index = len(self.question_options) // 2)

            st.divider()


    def display_questions_old(self, page_num):

        with st.form('page_form'):
        ## Main Question Loop
            for i in range(len(self.question_list)):
                quest = self.question_list[i]
                # weight = self.question_weights[i]

                quest_key = f'page{page_num}_question{i}'

                # self.question_keys.append(quest_key) ## potentiall superfluous

                answer = st.radio(f'Question {i + 1}: {quest}',
                                    self.question_options,
                                    horizontal = True,
                                    key = quest_key,
                                    index = len(self.question_options) // 2)

                st.divider()

            # Every form must have a submit button.
            submitted = st.form_submit_button('Submit')
            if submitted:
                self.store_answers(page_num)
                st.write('Answers stored, click the button below to move on!')

    def store_answers(self, page_num):

        # self.page_results = {persona: None for persona in self.personas}

        for i in range(len(self.question_list)):
            quest_key = f'page{page_num}_question{i}'
            # quest = self.question_list[i]
            answer = st.session_state.get(quest_key, None)
            weight = self.question_weights[i]

            # st.write(answer)
            if answer is not None:
                for persona in weight:
                    if self.page_results[persona] is None:
                        self.page_results[persona] = 0

                    self.page_results[persona] += weight[persona] * self.question_mapping[answer]

        st.session_state[f'page{page_num}_results'] = self.page_results

# class TestClass():
#     def __init__(self):
#         self.test_text = ''
#
#     def addText(self, text_to_add):
#         print(f'Before {self.test_text}')
#         self.test_text += text_to_add
#         print(f'after {self.test_text}')
