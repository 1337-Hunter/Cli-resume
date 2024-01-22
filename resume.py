import argparse
from termcolor import colored

def get_resume_content(language='en'):
    resume_content_en = f"""
{colored('Name:', 'blue')} John Doe
{colored('Location:', 'blue')} Anytown, USA
{colored('Email:', 'blue')} john.doe@example.com
{colored('Phone:', 'blue')} (555) 123-4567
{colored('LinkedIn:', 'blue')} linkedin.com/in/johndoe
{colored('GitHub:', 'blue')} github.com/johndoe

{colored('Summary:', 'cyan')}
Results-driven software engineer with 5+ years of experience in full-stack development. Proven expertise in designing and implementing scalable and efficient solutions. Strong problem-solving and collaboration skills.

{colored('Skills:', 'cyan')}
- Programming Languages: {colored('JavaScript (Node.js, React), Python, Java', 'green')}
- Database: {colored('MySQL, MongoDB', 'green')}
- Web Technologies: {colored('HTML, CSS, RESTful APIs', 'green')}
- Version Control: {colored('Git', 'green')}
- Tools: {colored('Docker, Jenkins', 'green')}
- Agile/Scrum methodologies

{colored('Experience:', 'yellow')}

{colored('Software Engineer | XYZ Tech, Anytown, USA | Jan 2022 - Present', 'yellow')}
- Developed and maintained key features for the company's flagship product using {colored('React and Node.js', 'green')}.
- Collaborated with cross-functional teams to design and implement scalable solutions.
- Conducted code reviews and mentored junior developers.

{colored('Junior Software Engineer | ABC Solutions, Anytown, USA | Jun 2019 - Dec 2021', 'yellow')}
- Contributed to the development of a new customer portal using {colored('Java and Spring Boot', 'green')}.
- Collaborated with QA to ensure the quality and reliability of software releases.
- Participated in daily stand-ups and sprint planning meetings.

{colored('Education:', 'cyan')}

Bachelor of Science in Computer Science
University of Anytown, Anytown, USA | Graduated May 2019

{colored('Projects:', 'cyan')}

1. {colored('ProjectX', 'green')} - GitHub: {colored('github.com/johndoe/projectx', 'blue')}
   - Description: Developed a scalable RESTful API using {colored('Node.js and MongoDB', 'green')} for real-time data processing.

2. {colored('Portfolio Website', 'green')} - GitHub: {colored('github.com/johndoe/portfolio', 'blue')}
   - Description: Designed and implemented a personal portfolio website using {colored('React', 'green')} and deployed it on {colored('Netlify', 'green')}.

{colored('Certifications:', 'cyan')}

- {colored('AWS Certified Developer – Associate', 'green')}
- {colored('Scrum Master Certification', 'green')}
"""

    resume_content_my = f"""
{colored('Nama:', 'blue')} John Doe
{colored('Lokasi:', 'blue')} Bandar Mana-saja, USA
{colored('Emel:', 'blue')} john.doe@example.com
{colored('Telefon:', 'blue')} (555) 123-4567
{colored('LinkedIn:', 'blue')} linkedin.com/in/johndoe
{colored('GitHub:', 'blue')} github.com/johndoe

{colored('Ringkasan:', 'cyan')}
Jurutera perisian berprestasi dengan lebih dari 5 tahun pengalaman dalam pembangunan sepenuhnya. Kecekapan terbukti dalam reka bentuk dan pelaksanaan penyelesaian yang boleh dikembangkan dan efisien. Kemahiran dalam penyelesaian masalah yang baik dan kerjasama yang kuat.

{colored('Kemahiran:', 'cyan')}
- Bahasa Pengaturcaraan: {colored('JavaScript (Node.js, React), Python, Java', 'green')}
- Pangkalan Data: {colored('MySQL, MongoDB', 'green')}
- Teknologi Web: {colored('HTML, CSS, RESTful APIs', 'green')}
- Kawalan Versi: {colored('Git', 'green')}
- Alat: {colored('Docker, Jenkins', 'green')}
- Metodologi Agile/Scrum

{colored('Pengalaman:', 'yellow')}

{colored('Jurutera Perisian | XYZ Tech, Bandar Mana-saja, USA | Jan 2022 - Kini', 'yellow')}
- Membangunkan dan mengekalkan ciri utama untuk produk unggulan syarikat menggunakan {colored('React dan Node.js', 'green')}.
- Berkolaborasi dengan pasukan lintas fungsi untuk merancang dan melaksanakan penyelesaian yang boleh dikembangkan.
- Melakukan semakan kod dan membimbing jurutera muda.

{colored('Jurutera Perisian Junior | ABC Solutions, Bandar Mana-saja, USA | Jun 2019 - Dis 2021', 'yellow')}
- Menyumbang kepada pembangunan portal pelanggan baru menggunakan {colored('Java dan Spring Boot', 'green')}.
- Berkolaborasi dengan QA untuk memastikan kualiti dan kebolehpercayaan pelepasan perisian.
- Mengambil bahagian dalam pertemuan berdiri dan perancangan sprints harian.

{colored('Pendidikan:', 'cyan')}

Ijazah Sarjana Muda dalam Sains Komputer
Universiti Mana-saja, Bandar Mana-saja, USA | Lulus Mei 2019

{colored('Projek:', 'cyan')}

1. {colored('ProjectX', 'green')} - GitHub: {colored('github.com/johndoe/projectx', 'blue')}
   - Penerangan: Membangunkan API RESTful yang boleh dikembangkan menggunakan {colored('Node.js dan MongoDB', 'green')} untuk pemprosesan data secara real-time.

2. {colored('Laman Web Portfolio', 'green')} - GitHub: {colored('github.com/johndoe/portfolio', 'blue')}
   - Penerangan: Mereka bentuk dan melaksanakan laman web portfolio peribadi menggunakan {colored('React', 'green')} dan diterbitkan di {colored('Netlify', 'green')}.

{colored('Sijil-sijil:', 'cyan')}

- {colored('Pengembang Berlesen AWS – Associate', 'green')}
- {colored('Sijil Master Scrum', 'green')}
"""

    if language.lower() == 'my':
        return resume_content_my
    else:
        return resume_content_en

def display_resume():
    print("Select language:")
    print("1. English (en)")
    print("2. Malay (my)")

    language_choice = input("Enter the language code (en/my): ").lower()

    if language_choice not in ['en', 'my']:
        print("Invalid language choice. Defaulting to English.")
        language_choice = 'en'

    resume_content = get_resume_content(language_choice)
    print(resume_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display a super cool CLI resume.")
    parser.parse_args()
    display_resume()
