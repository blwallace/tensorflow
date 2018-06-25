import tensorflow as tf
import pandas as pd


# Import NCAA Basketball data from CSV file.  Parse input and output
def input():
    win_loss_data = pd.read_csv('data/wl_spread_2015.csv')
    win_loss_historic = tf.to_float(
        win_loss_data[['spread_1', 'spread_2', 'spread_3', 'spread_4', 'spread_5']].as_matrix(),
        name='win_loss_historic')
    win_loss_current = tf.to_float(win_loss_data[['spread_0']].as_matrix().flatten(), name='win_loss_current')
    return win_loss_historic, win_loss_current


# Create weight, bias, and a way to combine data
with tf.name_scope('input_scope'):
    W = tf.Variable(tf.zeros([5, 1]), name='weights')
    b = tf.Variable(0., name='bias')

def inference(x):
    return tf.matmul(x, W) + b

# We want to minimize the loss between the actual spread and the model spread
def loss(X, spread_actual):
    spread_predicted = tf.transpose(inference(X))
    return tf.reduce_sum(tf.squared_difference(spread_actual, spread_predicted))

# Train the model
def train(total_loss):
    learning_rate = 0.0000001
    return tf.train.GradientDescentOptimizer(learning_rate).minimize(total_loss)

# Run model for UC Berkeley Mens Basketball
def eval_cal(sess):
    print('\n')
    print('2011 Cal Golden Bears: Actual Spead = ')
    print('14')
    print('2011 Cal Golden Bears: Estimated Spead = ')
    print(sess.run(inference([[3., 13., 11., 1., -1.]])))
    print('\n')
    print('2012 Cal Golden Bears: : Actual Spead = ')
    print('9')
    print('2012 Cal Golden Bears: : Estimated Spead = ')
    print(sess.run(inference([[14., 3., 13., 11., 1.]])))
    print('\n')
    print('2013 Cal Golden Bears: : Actual Spead = ')
    print('7')
    print('2013 Cal Golden Bears: : Estimated Spead = ')
    print(sess.run(inference([[9., 14., 3., 13., 11.]])))
    print('\n')
    print('2014 Cal Golden Bears: : Actual Spead = ')
    print('3')
    print('2014 Cal Golden Bears: : Estimated Spead = ')
    print(sess.run(inference([[7., 9., 14., 3., 13.]])))
    print('\n')
    print('2015 Cal Golden Bears: : Actual Spead = ')
    print('13')
    print('2015 Cal Golden Bears: : Estimated Spead = ')
    print(sess.run(inference([[13., 3., 7., 9., 14.]])))
    print('\n')

# Run model for Stanford Mens Basketball
def eval_stanford(sess):
    print('2011 Stanford Cardinals: Actual Spead = ')
    print('15')
    print('2011 Stanford Cardinals: Estimated Spead = ')
    print(sess.run(inference([[-1.,-4.,6.,20.,5.]])))
    print('\n')
    print('2012 Stanford Cardinals: : Actual Spead = ')
    print('4')
    print('2012 Stanford Cardinals: : Estimated Spead = ')
    print(sess.run(inference([[15.,-1.,-4.,6.,20.]])))
    print('\n')
    print('2013 Stanford Cardinals: : Actual Spead = ')
    print('10')
    print('2013 Stanford Cardinals: : Estimated Spead = ')
    print(sess.run(inference([[4.,15.,-1.,-4.,6.]])))
    print('\n')
    print('2014 Stanford Cardinals: : Actual Spead = ')
    print('11')
    print('2014 Stanford Cardinals: : Estimated Spead = ')
    print(sess.run(inference([[10.,4.,15.,-1.,-4.]])))
    print('\n')
    print('2015 Stanford Cardinals: : Actual Spead = ')
    print('0')
    print('2015 Stanford Cardinals: : Estimated Spead = ')
    print(sess.run(inference([[11.,10.,4.,15.,-1.]])))
    print('\n')




with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)

    X, Y = input()
    total_loss = loss(X, Y)
    train_op = train(total_loss)

    # Run training loop
    training_steps = 10000
    for step in range(training_steps):
        sess.run([train_op])
        # Print results
        if step % 1000 == 0:
            print('Epoch: ' + str(step) + ' loss: ')
            print(sess.run(total_loss))

    print('Final model W=')
    print(sess.run(W))
    print('Final model b=')
    print(sess.run(b))

    eval_cal(sess)
    eval_stanford(sess)

    sess.close()
