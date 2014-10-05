from collections import OrderedDict
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Text

from lab.model.meta import Base

koan_dict = OrderedDict([
    ("Joshu's Dog", [
        """A monk asked Joshu, a Chinese Zen master: "Has a dog Buddha-nature or not?" """,
        """Joshu answered: "Mu." """
    ]),
    ("Hyakujo's Fox", [
        """Once when Hyakujo delivered some Zen lectures an old man attended them, unseen by the monks. At the end of each talk when the monks left so did he. But one day he remained after they had gone, and Hyakujo asked him: "Who are you?" """,
        """The old man replied: "I am not a human being, but I was a human being when the Kashapa Buddha preached in this world. I was a Zen master and lived on this mountain. At that time one of my students asked me whether or not the enlightened man is subject to the law of causation. I answered him: 'The enlightened man is not subject to the law of causation.' For this answer evidencing a clinging to absoluteness I became a fox for five hundred rebirths, and I am still a fox. Will you save me from this condition with your Zen words and let me get out of a fox's body? Now may I ask you: Is the enlightened man subject to the law of causation?" """,
        """Hyakujo said: "The enlightened man is one with the law of causation." """,
        """At the words of Hyakujo the old man was enlightened. "I am emancipated," he said, paying homage with a deep bow. "I am no more a fox, but I have to leave my body in my dwelling place behind this mountain. Please perform my funeral as a monk." Then he disappeared.""",
        """The next day Hyakujo gave an order through the chief monk to prepare to attend the funeral of a monk. "No one was sick in the infirmary," wondered the monks. "What does our teacher mean?" """,
        """After dinner Hyakujo led the monks out and around the mountain. In a cave, with his staff he poked out the corpse of an old fox and then performed the ceremony of cremation.""",
        """That evening Hyakujo gave a talk to the monks and told them this story about the law of causation.""",
        """Obaku, upon hearing the story, asked Hyakujo: "I understand that a long time ago because a certain person gave a wrong Zen answer he became a fox for five hundred rebirths. Now I want to ask: If some modern master is asked many questions and he always gives the right answer, what will become of him?" """,
        """Hyakujo said: "You come here near me and I will tell you." """,
        """Obaku went near Hyakujo and slapped the teacher's face with his hand, for he knew this was the answer his teacher intended to give him.""",
        """Hyakujo clapped his hands and laughed at this discernment. "I thought a Persian had a red beard," he said, "and now I know a Persian who has a red beard." """
    ]),
    ("Gutei's Finger", [
        """Gutei raised his finger whenever he was asked a question about Zen. A boy attendant began to imitate him in this way. When anyone asked the boy what his master had preached about, the boy would raise his finger.""",
        """Gutei heard about the boy's mischief. He seized him and cut off his finger. The boy cried and ran away. Gutei called and stopped him. When the boy turned his head to Gutei, Gutei raised up his own finger. In that instant the boy was enlightened.""",
        """When Gutei was about to pass from this world he gathered his monks around him. "I attained my finger-Zen," he said, "from my teacher Tenryu, and in my whole life I could not exhaust it." Then he passed away."""
    ]),
    ("A Beardless Foreigner", [
        """Wakuan complained when he saw a picture of bearded Bodhidharma: "Why hasn't that fellow a beard?" """
    ]),
    ("Kyogen Mounts the Tree", [
        """Kyogen said: "Zen is like a man hanging in a tree by his teeth over a precipice. His hands grasp no branch, his feet rest on no limb, and under the tree another person asks him: 'Why did Bodhidharma come to China from India?'""",
        """ "If the man in the tree does not answer, he fails; and if he does answer, he falls and loses his life. Now what shall he do?" """
    ]),
    ("Buddha Twirls a Flower", [
        """When Buddha was in Grdhrakuta mountain he turned a flower in his fingers and held it before his listeners. Every one was silent. Only Maha-Kashapa smiled at this revelation, although he tried to control the lines of his face.""",
        """Buddha said: "I have the eye of the true teaching, the heart of Nirvana, the true aspect of non-form, and the ineffable stride of Dharma. It is not expressed by words, but especially transmitted beyond teaching. This teaching I have given to Maha-Kashapa." """
    ]),
    ("Joshu Washes the Bowl", [
        """A monk told Joshu: "I have just entered the monastery. Please teach me." """,
        """Joshu asked: "Have you eaten your rice porridge?" """,
        """The monk replied: "I have eaten." """,
        """Joshu said: "Then you had better wash your bowl." """,
        """At that moment the monk was enlightened. """
    ]),
    ("Keichu's Wheel", [
        """Getsuan said to his students: "Keichu, the first wheel-maker of China, made two wheels of fifty spokes each. Now, suppose you removed the nave uniting the spokes. What would become of the wheel? And had Keichu done this, could he be called the master wheel-maker?" """
    ]),
    ("A Buddha before History", [
        """A monk asked Seijo: "I understand that a Buddha who lived before recorded history sat in meditation for ten cycles of existence and could not realize the highest truth, and so could not become fully emancipated. Why was this so?" """,
        """Seijo replied: "Your question is self-explanatory." """,
        """The monk asked: "Since the Buddha was meditating, why could he not fulfill Buddhahood?" """,
        """Seijo said: "He was not a Buddha." """
    ]),
    ("Seizei Alone and Poor", [
        """A monk named Seizei asked of Sozan: "Seizei is alone and poor. Will you give him support?" """,
        """Sozan asked: "Seizei?" """,
        """Seizei responded: "Yes, sir." """,
        """Sozan said: "You have Zen, the best wine in China, and already have finished three cups, and still you are saying that they did not even wet your lips." """
    ]),
    ("Joshu Examines a Monk in Meditation", [
        """Joshu went to a place where a monk had retired to meditate and asked him: "What is, is what?" """,
        """The monk raised his fist.""",
        """Joshu replied: "Ships cannot remain where the water is too shallow." And he left.""",
        """A few days later Joshu went again to visit the monk and asked the same question.""",
        """The monk answered the same way.""",
        """Joshu said: "Well given, well taken, well killed, well saved." And he bowed to the monk."""
    ]),
    ("Zuigan Calls His Own Master", [
        """Zuigan called out to himself every day: "Master." """,
        """Then he answered himself: "Yes, sir." """,
        """And after that he added: "Become sober." """,
        """Again he answered: "Yes, sir." """,
        """ "And after that," he continued, "do not be deceived by others." """,
        """ "Yes, sir; yes, sir," he answered."""
    ]),
    ("Tokusan Holds His Bowl", [
        """Tokusan went to the dining room from the meditation hall holding his bowl. Seppo was on duty cooking. When he met Tokusan he said: "The dinner drum is not yet beaten. Where are you going with your bowl?" """,
        """So Tokusan returned to his room.""",
        """Seppo told Ganto about this. Ganto said: "Old Tokusan did not understand ultimate truth." """,
        """Tokusan heard of this remark and asked Ganto to come to him. "I have heard," he said, "you are not approving my Zen." Ganto admitted this indirectly. Tokusan said nothing.""",
        """The next day Tokusan delivered an entirely different kind of lecture to the monks. Ganto laughed and clapped his hands, saying: "I see our old man understands ultimate truth indeed. None in China can surpass him." """
    ]),
    ("Nansen Cuts the Cat in Two", [
        """Nansen saw the monks of the eastern and western halls fighting over a cat. He seized the cat and told the monks: "If any of you say a good word, you can save the cat." """,
        """No one answered. So Nansen boldly cut the cat in two pieces.""",
        """That evening Joshu returned and Nansen told him about this. Joshu removed his sandals and, placing them on his head, walked out.""",
        """Nansen said: "If you had been there, you could have saved the cat." """
    ]),
    ("Tozan's Three Blows", [
        """Tozan went to Ummon. Ummon asked him where he had come from.""",
        """Tozan said: "From Sato village." """,
        """Ummon asked: "In what temple did you remain for the summer?" """,
        """Tozan replied: "The temple of Hoji, south of the lake." """,
        """ "When did you leave there?" asked Ummon, wondering how long Tozan would continue with such factual answers. """,
        """ "The twenty-fifth of August," answered Tozan. """,
        """Ummon said: "I should give you three blows with a stick, but today I forgive you." """,
        """The next day Tozan bowed to Ummon and asked: "Yesterday you forgave me three blows. I do not know why you thought me wrong." """,
        """Ummon, rebuking Tozan's spiritless responses, said: "You are good for nothing. You simply wander from one monastery to another." """,
        """Before Ummon's words were ended Tozan was enlightened. """
    ]),
    ("Bells and Robes", [
        """Ummon asked: "The world is such a wide world, why do you answer a bell and don ceremonial robes?" """
    ]),
    ("The Three Calls of the Emperor's Teacher", [
        """Chu, called Kokushi, the teacher of the emperor, called to his attendant: "Oshin." """,
        """Oshin answered: "Yes." """,
        """Chu repeated, to test his pupil: "Oshin." """,
        """Oshin repeated: "Yes." """,
        """Chu called: "Oshin." """,
        """Oshin answered: "Yes." """,
        """Chu said: "I ought to apologize to you for all this calling, but really you ought to apologize to me." """
    ]),
    ("Tozan's Three Pounds", [
        """A monk asked Tozan when he was weighing some flax: "What is Buddha?" """,
        """Tozan said: "This flax weighs three pounds." """
    ]),
    ("Everyday Life Is the Path", [
        """Joshu asked Nansen: "What is the path?" """,
        """Nansen said: "Everyday life is the path." """,
        """Joshu asked: "Can it be studied?" """,
        """Nansen said: "If you try to study, you will be far away from it." """,
        """Joshu asked: "If I do not study, how can I know it is the path?" """,
        """Nansen said: "The path does not belong to the perception world, neither does it belong to the nonperception world. Cognition is a delusion and noncognition is senseless. If you want to reach the true path beyond doubt, place yourself in the same freedom as sky. You name it neither good nor not-good." """,
        """At these words Joshu was enlightened. """
    ]),
    ("The Enlightened Man", [
        """Shogen asked: "Why does the enlightened man not stand on his feet and explain himself?" And he also said: "It is not necessary for speech to come from the tongue." """
    ]),
    ("Dried Dung", [
        """A monk asked Ummon: "What is Buddha?" """,
        """Ummon answered him: "Dried dung." """
    ]),
    ("Kashapa's Preaching Sign", [
        """Ananda asked Kashapa: "Buddha gave you the golden-woven robe of successorship. What else did he give you?" """,
        """Kashapa said: "Ananda." """,
        """Ananda answered: "Yes, brother." """,
        """Said Kashapa: "Now you can take down my preaching sign and put up your own." """
    ]),
    ("Do Not Think Good, Do Not Think Not-Good", [
        """When he became emancipated the sixth patriarch received from the fifth patriarch the bowl and robe given from the Buddha to his successors, generation after generation. """,
        """A monk named E-myo out of envy pursued the patriarch to take this great treasure away from him. The sixth patriarch placed the bowl and robe on a stone in the road and told E-myo: "These objects just symbolize the faith. There is no use fighting over them. If you desire to take them, take them now." """,
        """When E-myo went to move the bowl and robe they were as heavy as mountains. He could not budge them. Trembling for shame he said: "I came wanting the teaching, not the material treasures. Please teach me." """,
        """The sixth patriarch said: "When you do not think good and when you do not think not-good, what is your true self?" """,
        """At these words E-myo was illumined. Perspiration broke out all over his body. He cried and bowed, saying: "You have given me the secret words and meanings. Is there yet a deeper part of the teaching?" """,
        """The sixth patriarch replied: "What I have told you is no secret at all. When you realize your own true self the secret belongs to you." """,
        """E-myo said: "I was under the fifth patriarch many years but could not realize my true self until now. Through your teaching I find the source. A person drinks water and knows himself whether it is cold or warm. May I call you my teacher?" """,
        """The sixth patriarch replied: "We studied together under the fifth patriarch. Call him your teacher, but just treasure what you have attained." """
    ]),
    ("Without Words, Without Silence", [
        """A monk asked Fuketsu: "Without speaking, without silence, how can you express the truth?" """,
        """Fuketsu observed: "I always remember springtime in southern China. The birds sing among innumerable kinds of fragrant flowers." """
    ]),
    ("Preaching from the Third Seat", [
        """In a dream Kyozan went to Maitreya's Pure Land. He recognized himself seated in the third seat in the abode of Maitreya. Someone announced: "Today the one who sits in the third seat will preach." """,
        """Kyozan arose and, hitting the gavel, said: "The truth of Mahayana teaching is transcendent, above words and thought. Do you understand?" """
    ]),
    ("Two Monks Roll Up the Screen", [
        """Hogen of Seiryo monastery was about to lecture before dinner when he noticed that the bamboo screen lowered for meditation had not been rolled up. He pointed to it. Two monks arose from the audience and rolled it up. """,
        """Hogen, observing the physical moment, said: "The state of the first monk is good, not that of the other." """
    ]),
    ("It Is Not Mind, It Is Not Buddha, It Is Not Things", [
        """A monk asked Nansen: "Is there a teaching no master ever preached before?" """,
        """Nansen said: "Yes, there is." """,
        """ "What is it?" asked the monk. """,
        """Nansen replied: "It is not mind, it is not Buddha, it is not things." """
    ]),
    ("Blow Out the Candle", [
        """Tokusan was studying Zen under Ryutan. One night he came to Ryutan and asked many questions. The teacher said: "The night is getting old. Why don't you retire?" """,
        """So Tokusan bowed and opened the screen to go out, observing: "It is very dark outside." """,
        """Ryutan offered Tokusan a lighted candle to find his way. Just as Tokusan received it, Ryutan blew it out. At that moment the mind of Tokusan was opened. """,
        """ "What have you attained?" asked Ryutan. "From now on," said Tokusan, "I will not doubt the teacher's words." """,
        """The next day Ryutan told the monks at his lecture: "I see one monk among you. His teeth are like the sword tree, his mouth is like the blood bowl. If you hit him hard with a big stick, he will not even so much as look back at you. Someday he will mount the highest peak and carry my teaching there." """,
        """On that day, in front of the lecture hall, Tokusan burned to ashes his commentaries on the sutras. He said: "However abstruse the teachings are, in comparison with this enlightenment they are like a single hair to the great sky. However profound the complicated knowledge of the world, compared to this enlightenment it is like one drop of water to the great ocean." Then he left that monastery. """
    ]),
    ("Not the Wind, Not the Flag", [
        """Two monks were arguing about a flag. One said: "The flag is moving." """,
        """The other said: "The wind is moving." """,
        """The sixth patriarch happened to be passing by. He told them: "Not the wind, not the flag; mind is moving." """
    ]),
    ("This Mind Is Buddha", [
        """Daibai asked Baso: "What is Buddha?" """,
        """Baso said: "This mind is Buddha." """
    ]),
    ("Joshu Investigates", [
        """A traveling monk asked an old woman the road to Taizan, a popular temple supposed to give wisdom to the one who worships there. The old woman said: "Go straight ahead." When the monk proceeded a few steps, she said to herself: "He also is a common church-goer." """,
        """Someone told this incident to Joshu, who said: "Wait until I investigate." The next day he went and asked the same question, and the old woman gave the same answer. """,
        """Joshu remarked: "I have investigated that old woman." """
    ]),
    ("A Philosopher Asks Buddha", [
        """A philosopher asked Buddha: "Without words, without the wordless, will you tell me truth?" """,
        """The Buddha kept silence. """,
        """The philosopher bowed and thanked the Buddha, saying: "With your loving kindness I have cleared away my delusions and entered the true path." """,
        """After the philosopher had gone, Ananda asked the Buddha what he had attained. """,
        """The Buddha replied: "A good horse runs even at the shadow of the whip." """
    ]),
    ("This Mind Is Not Buddha", [
        """A monk asked Baso: "What is Buddha?" """,
        """Baso said: "This mind is not Buddha." """
    ]),
    ("Learning Is Not the Path", [
        """Nansen said: "Mind is not Buddha. Learning is not the path." """
    ]),
    ("Two Souls", [
        """ "Seijo, the Chinese girl," observed Goso, "had two souls, one always sick at home and the other in the city, a married woman with two children. Which was the true soul?" """
    ]),
    ("Meeting a Zen Master on the Road", [
        """Goso said: "When you meet a Zen master on the road you cannot talk to him, you cannot face him with silence. What are you going to do?" """
    ]),
    ("A Buffalo Passes Through the Enclosure", [
        """Goso said: "When a buffalo goes out of his enclosure to the edge of the abyss, his horns and his head and his hoofs all pass through, but why can't the tail also pass?" """
    ]),
    ("An Oak Tree in the Garden", [
        """A monk asked Joshu why Bodhidharma came to China. """,
        """Joshu said: "An oak tree in the garden." """
    ]),
    ("Ummon's Sidetrack", [
        """A Zen student told Ummon: "Brilliancy of Buddha illuminates the whole universe." """,
        """Before he finished the phrase Ummon asked: "You are reciting another's poem, are you not?" """,
        """ "Yes," answered the student. """,
        """ "You are sidetracked," said Ummon. """,
        """Afterwards another teacher, Shishin, asked his pupils: "At what point did that student go off the track?" """
    ]),
    ("Tipping Over a Water Vase", [
        """Hyakujo wished to send a monk to open a new monastery. He told his pupils that whoever answered a question most ably would be appointed. Placing a water vase on the ground, he asked: "Who can say what this is without calling its name?" """,
        """The chief monk said: "No one can call it a wooden shoe." """,
        """Isan, the cooking monk, tipped over the vase with his foot and went out. """,
        """Hyakujo smiled and said: "The chief monk loses." And Isan became the master of the new monastery. """
    ]),
    ("Bodhidharma Pacifies the Mind", [
        """Bodhidharma sits facing the wall. His future successor stands in the snow and presents his severed arm to Bodhidharma. He cries: "My mind is not pacified. Master, pacify my mind." """,
        """Bodhidharma says: "If you bring me that mind, I will pacify it for you." """,
        """The successor says: "When I search my mind I cannot hold it." """,
        """Bodhidharma says: "Then your mind is pacified already." """
    ]),
    ("The Girl Comes Out from Meditation", [
        """In the time of Buddha Shakyamuni, Manjusri went to the assemblage of the Buddhas. When he arrived there, the conference was over and each Buddha had returned to his own Buddha-land. Only one girl was yet unmoved in deep meditation. """,
        """Manjusri asked Buddha Shakyamuni how it was possible for this girl to reach this state, one which even he could not attain. "Bring her out from Samadhi and ask her yourself," said the Buddha. """,
        """Manjusri walked around the girl three times and snapped his fingers. She still remained in meditation. So by his miracle power he transported her to a high heaven and tried his best to call her, but in vain. """,
        """Buddha Shakyamuni said: "Even a hundred thousand Manjusris could not disturb her, but below this place, past twelve hundred million countries, is a Bodhisattva, Mo-myo, seed of delusion. If he comes here, she will awaken." """,
        """No sooner had the Buddha spoken than that Bodhisattva sprang up from the earth and bowed and paid homage to the Buddha. Buddha directed him to arouse the girl. The Bodhisattva went in front of the girl and snapped his fingers, and in that instant the girl came out from her deep meditation. """
    ]),
    ("Shuzan's Short Staff", [
        """Shuzan held out his short staff and said: "If you call this a short staff, you oppose its reality. If you do not call it a short staff, you ignore the fact. Now what do you wish to call this?" """
    ]),
    ("Basho's Staff", [
        """Basho said to his disciple: "When you have a staff, I will give it to you. If you have no staff, I will take it away from you." """
    ]),
    ("Who Is He?", [
        """Hoen said: "The past and future Buddhas, both are his servants. Who is he?" """
    ]),
    ("Proceed from the Top of the Pole", [
        """Sekiso asked: "How can you proceed on from the top of a hundred-foot pole?" Another Zen teacher said: "One who sits on the top of a hundred-foot pole has attained a certain height but still is not handling Zen freely. He should proceed on from there and appear with his whole body in the ten parts of the world." """
    ]),
    ("Three Gates of Tosotsu", [
        """Tosotsu built three barriers and made the monks pass through them. The first barrier is studying Zen. In studying Zen the aim is to see one's own true nature. Now where is your true nature? """,
        """Secondly, when one realizes his own true nature he will be free from birth and death. Now when you shut the light from your eyes and become a corpse, how can you free yourself? """,
        """Thirdly, if you free yourself from birth and death, you should know where you are. Now your body separates into the four elements. Where are you? """
    ]),
    ("One Road of Kembo", [
        """A Zen pupil asked Kembo: "All Buddhas of the ten parts of the universe enter the one road of Nirvana. Where does that road begin?" """,
        """Kembo, raising his walking stick and drawing the figure one in the air, said: "Here it is." """,
        """This pupil went to Ummon and asked the same question. Ummon, who happened to have a fan in his hand, said: "This fan will reach to the thirty-third heaven and hit the nose of the presiding deity there. It is like the Dragon Carp of the Eastern Sea tipping over the rain-cloud with his tail." """
    ])
])

class Koan(Base):
    __tablename__ = 'koan'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    text = Column(Text)

    def __init__(self, title='', text=''):
        self.title = title
        self.text = text

    def __repr__(self):
        return "<Koan('{title}')>".format(title=self.title)
