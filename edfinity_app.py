#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import streamlit as st




def process_edfinity_upload(): #Create File

    uploaded_file = st.file_uploader("Upload Files", type = ['csv'])
    if uploaded_file is not None:
        file_details = {"FileName":uploaded_file.name, "FileType":uploaded_file.type, "FileSize":uploaded_file.size}
        st.write(file_details)
        edfinity_raw = pd.read_csv(uploaded_file)
        edf=edfinity_raw
        edf = edf[edf.columns.drop(list(edf.filter(regex='(Preview)')))]
        regularization_list=edf.drop(columns=['Last Name', 'First Name', 'Email/Username', 'ID', 'Course Name', 'Review of Prerequisites for Calculus I']).columns
        edf=edf.drop(columns='Review of Prerequisites for Calculus I')
        for column in regularization_list:
            edf[column]=((edf[column]/(edf[edf['First Name']=='Possible'][column].values))>=.8).astype(int)
        edf=edf.drop('ID', axis=1)
        #edf=edf.drop(0, axis=0) #Drop Points Possible Row
        #assignment_list=['Edfinity '+item[0] for item in edf.columns[5:].str.split(' ')]
        st.dataframe(edf)
        if st.button('Remove Assigments with No Successes'):
            edf_summary=edf.sum(axis=0)
            edf=edf[edf.columns.drop(list(edf_summary[edf_summary==1].index))]
            st.dataframe(edf)
            #st.dataframe(edf_summary)

        st.download_button(label="Download File", data=edf.to_csv(), mime='text/csv', file_name='processed_edfinity.csv')


def main():
    st.title("Mastery-Based Grading Edfinity Conversion")
    process_edfinity_upload()


if __name__ == "__main__":
    main()
