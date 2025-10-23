import pandas as pd
import numpy as np

df = pd.read_csv('lab01_train.csv')
#df.head()
df.tail(10)

number_of_request_course_2 = df['course_2'].notna().sum()
number_of_request_course_3 = df['course_3'].notna().sum()

print('Кол-во заявок от 2 курса:', number_of_request_course_2)
print('Кол-во заявок от 3 курса:', number_of_request_course_3)

is_equal_percentil = df['percentile'].duplicated().any()
print(f'Наличие дубликатов: {is_equal_percentil}')

course_2_na = df['course_2'].isna().sum()
course_3_na = df['course_3'].isna().sum()
is_mi_student_na = df['is_mi_student'].isna().sum()
is_ml_student_na = df['is_ml_student'].isna().sum()
is_first_time_na = df['is_first_time'].isna().sum()
blended_na = df['blended'].isna().sum()
percentile_na = df['percentile'].isna().sum()

df_copy = df.copy()
str_cols = ['course_2', 'course_3', 'blended']
digit_cols = ['is_mi_student', 'is_ml_student']
df_copy[str_cols] = df_copy[str_cols].fillna('')
df_copy[digit_cols] = df_copy[digit_cols].fillna(0)

df_na = (df.isna().sum() == 0).all()

number_is_first_time_responses_no = (df['is_first_time'] == 'Нет').sum()

df_copy['timestamp'] = pd.to_datetime(df_copy['timestamp']) # чтобы pandas понимал, что это дата/время, а не просто строки
df_copy_sorted = df_copy.sort_values(['id', 'timestamp'], ascending=[True, False]) # сортируем по id (возрастание) и timestamp (убыванию) новейшие сверху
df_copy_unique = df_copy_sorted.drop_duplicates(subset='id', keep='first') # ищем дупликаты в id и оставляем только first
total_number_of_request = len(df_copy_unique)

print(total_number_of_request)

blended_courses_for_second_year_students = {*df[df['course_2'].notna()]['blended'].unique()}

blended_course_with_max_request = df['blended'].value_counts().index[0]

melted_courses = pd.melt(df,
                        id_vars=['rating'],
                        value_vars=['fall_1', 'fall_2', 'fall_3', 'spring_1', 'spring_2', 'spring_3', 'blended'],
                        var_name='semester',
                        value_name='course')

course_ratings = melted_courses.dropna(subset=['course']).groupby('course')['rating'].mean()

course_with_highest_average_rating = course_ratings.idxmax()
print(f"Курс с самым высоким средним рейтингом: {course_with_highest_average_rating}")

course_cols = ['fall_1', 'fall_2', 'fall_3', 'spring_1', 'spring_2', 'spring_3', 'blended']
duplicates = df_copy_unique.duplicated(subset=course_cols, keep=False)
number_duplicate_sets_of_courses = duplicates.sum()

print(f"Количество дублирующихся наборов курсов: {number_duplicate_sets_of_courses}")

duplicate_sets_of_courses_with_number_students = df_copy_unique.groupby(course_cols).size().reset_index(name='number_of_students')

duplicate_sets_of_courses_with_number_students = duplicate_sets_of_courses_with_number_students[duplicate_sets_of_courses_with_number_students['number_of_students'] > 1]

duplicate_sets_of_courses_with_number_students = duplicate_sets_of_courses_with_number_students.sort_values('spring_1', ascending=False)

print("Дублирующиеся наборы курсов с количеством студентов:")
duplicate_sets_of_courses_with_number_students.head(50)